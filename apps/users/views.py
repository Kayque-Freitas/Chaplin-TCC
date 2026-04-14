from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile, ActivityLog, Especialidade
from .forms import UserRegistrationForm
from django.db.models import Q
from django.core.paginator import Paginator
from apps.tasks.views import _is_manager
import pyotp
from django.core.cache import cache
import random
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserRegistrationForm, EmailVerificationForm

def login_view(request):
    ip = request.META.get('REMOTE_ADDR', '')
    cache_key = f"login_fails_{ip}"
    fails = cache.get(cache_key, 0)

    if fails >= 5:
        return render(request, 'users/login.html', {'error': 'Muitas tentativas fracassadas. O acesso está bloqueado por 5 minutos.'})

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            cache.delete(cache_key)
            profile = getattr(user, 'profile', None)
            if profile and profile.two_factor_enabled and profile.totp_secret:
                # Store user id in session for 2FA step (don't log in yet)
                request.session['pre2fa_user_id'] = user.id
                request.session['pre2fa_user_backend'] = user.backend
                return redirect('users:two_factor_verify')
            login(request, user)
            return redirect('tasks:dashboard')
        else:
            cache.set(cache_key, fails + 1, timeout=300)
            return render(request, 'users/login.html', {'error': 'Usuário ou senha inválidos. Tente novamente.'})
    return render(request, 'users/login.html')


@login_required
def setup_2fa_view(request):
    """Exibe o QR code TOTP e pede confirmação do código para ativar 2FA."""
    profile = request.user.profile
    # Gerar um novo segredo se não existir
    if not profile.totp_secret:
        profile.totp_secret = pyotp.random_base32()
        profile.save()

    totp = pyotp.TOTP(profile.totp_secret)
    otp_uri = totp.provisioning_uri(
        name=request.user.email or request.user.username,
        issuer_name='Chaplin'
    )

    error = None
    if request.method == 'POST':
        code = request.POST.get('code', '').strip()
        if totp.verify(code, valid_window=1):
            profile.two_factor_enabled = True
            profile.save()
            messages.success(request, '2FA ativado com sucesso!')
            return redirect('tasks:settings')
        else:
            error = 'Código inválido. Verifique o app autenticador e tente novamente.'

    return render(request, 'users/two_factor_setup.html', {
        'otp_uri': otp_uri,
        'secret': profile.totp_secret,
        'error': error,
    })


@login_required
def disable_2fa_view(request):
    """Desativa 2FA após confirmar a senha."""
    profile = request.user.profile
    error = None
    if request.method == 'POST':
        password = request.POST.get('password', '')
        user = authenticate(request, username=request.user.username, password=password)
        if user is not None:
            profile.two_factor_enabled = False
            profile.totp_secret = ''
            profile.save()
            messages.success(request, '2FA desativado com sucesso.')
            return redirect('tasks:settings')
        else:
            error = 'Senha incorreta. Tente novamente.'
    return render(request, 'users/two_factor_disable.html', {'error': error})


def two_factor_verify_view(request):
    """Verificação do código TOTP durante o login."""
    user_id = request.session.get('pre2fa_user_id')
    if not user_id:
        return redirect('users:login')

    user = get_object_or_404(User, pk=user_id)
    profile = getattr(user, 'profile', None)
    error = None

    if request.method == 'POST':
        code = request.POST.get('code', '').strip()
        totp = pyotp.TOTP(profile.totp_secret)
        if totp.verify(code, valid_window=1):
            backend = request.session.get('pre2fa_user_backend')
            if backend:
                user.backend = backend
            else:
                user.backend = 'apps.users.backends.EmailOrUsernameModelBackend'
            
            del request.session['pre2fa_user_id']
            if 'pre2fa_user_backend' in request.session:
                del request.session['pre2fa_user_backend']
            login(request, user)
            return redirect('tasks:dashboard')
        else:
            error = 'Código inválido. Tente novamente.'

    return render(request, 'users/two_factor_verify.html', {
        'username': user.get_full_name() or user.username,
        'error': error,
    })


def logout_view(request):
    logout(request)
    return redirect('core:index')

def register_view(request):
    """View para registrar novos usuários (Pública)"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.is_active = False # Conta travada até validar o e-mail
            user.save()
            
            profile = user.profile
            profile.role = form.cleaned_data.get('role', 'gestor')
            profile.cpf = form.cleaned_data.get('cpf', '')
            profile.cnpj = form.cleaned_data.get('cnpj', '')
            
            code = str(random.randint(100000, 999999))
            profile.email_verification_code = code
            profile.email_code_expires_at = timezone.now() + timedelta(minutes=15)
            profile.save()
            
            # Enviar E-mail
            try:
                send_mail(
                    subject='[Chaplin] Seu código de ativação',
                    message=f'Olá {user.first_name},\n\nSeu código de ativação de 6 dígitos é: {code}\nEle expira em 15 minutos.',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user.email],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Erro ao enviar email: {e}")
                
            request.session['verify_user_id'] = user.id
            messages.info(request, f'Pronto! Enviamos um código de segurança de 6 dígitos para o e-mail {user.email}.')
            return redirect('users:verify_email')
    else:
        form = UserRegistrationForm()
        
    return render(request, 'users/register.html', {'form': form})

def verify_email_code_view(request):
    """Visualização pública para validar o OTP do E-mail e ativar a conta"""
    user_id = request.session.get('verify_user_id')
    if not user_id:
        return redirect('users:register')
        
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        form = EmailVerificationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('code')
            profile = getattr(user, 'profile', None)
            
            if not profile or not profile.email_verification_code:
                messages.error(request, 'Nenhum código gerado para este usuário.')
            elif profile.email_code_expires_at and profile.email_code_expires_at < timezone.now():
                messages.error(request, 'Este código expirou. Realize o cadastro novamente.')
            elif profile.email_verification_code == code:
                user.is_active = True
                user.save()
                profile.email_verification_code = ''
                profile.save()
                del request.session['verify_user_id']
                messages.success(request, 'E-mail validado com sucesso! Você já pode entrar na plataforma.')
                return redirect('users:login')
            else:
                messages.error(request, 'Código inválido. Tente novamente.')
    else:
        form = EmailVerificationForm()
        
    return render(request, 'users/verify_email.html', {'form': form, 'email': user.email})

@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'users/profile.html', {'profile': profile})

def is_admin(user):
    return user.is_superuser or (hasattr(user, 'profile') and user.profile.role == 'admin')

@login_required
@user_passes_test(is_admin)
def admin_users_list_view(request):
    """View para o Administrador listar e buscar usuários"""
    query = request.GET.get('q', '')
    role_filter = request.GET.get('role', '')
    
    users_list = User.objects.all().order_by('-date_joined')
    
    if query:
        users_list = users_list.filter(
            Q(username__icontains=query) | 
            Q(email__icontains=query) |
            Q(first_name__icontains=query)
        )
    
    if role_filter:
        users_list = users_list.filter(profile__role=role_filter)
        
    paginator = Paginator(users_list, 10) # 10 usuários por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'query': query,
        'role_filter': role_filter,
        'roles': UserProfile.ROLE_CHOICES
    }
    return render(request, 'users/admin/list.html', context)

@login_required
@user_passes_test(is_admin)
def admin_user_edit_view(request, user_id):
    """View para editar um usuário específico (incluindo Role via Auditoria)"""
    target_user = get_object_or_404(User, id=user_id)
    especialidades = Especialidade.objects.all()
    
    if request.method == 'POST':
        # Dados básicos
        target_user.first_name = request.POST.get('first_name', target_user.first_name)
        target_user.last_name = request.POST.get('last_name', target_user.last_name)
        target_user.email = request.POST.get('email', target_user.email)
        
        # Perfil/Role
        new_role = request.POST.get('role')
        old_role = target_user.profile.role
        
        if new_role and new_role != old_role:
            target_user.profile.role = new_role
            if new_role == 'admin':
                target_user.is_superuser = True
                target_user.is_staff = True
            else:
                target_user.is_superuser = False
            
            # Registrar auditoria na mudança de patente
            ActivityLog.objects.create(
                admin_user=request.user,
                target_user=target_user,
                action='CHANGE_ROLE',
                role_old=old_role,
                role_new=new_role,
                ip_address=request.META.get('REMOTE_ADDR')
            )
            messages.success(request, f"Nível de conta alterado de {old_role} para {new_role}.")
            
        # Especialidade
        esp_id = request.POST.get('especialidade')
        if esp_id:
            target_user.profile.especialidade_id = esp_id
            
        target_user.save()
        target_user.profile.save()
        messages.success(request, "Usuário atualizado com sucesso.")
        return redirect('users:admin_users_list')
        
    return render(request, 'users/admin/edit.html', {
        'target_user': target_user,
        'roles': UserProfile.ROLE_CHOICES,
        'especialidades': especialidades
    })

@login_required
@user_passes_test(is_admin)
def admin_user_delete_view(request, user_id):
    """View para excluir ou desativar um usuário."""
    target_user = get_object_or_404(User, id=user_id)
    
    # Não permitir que o admin exclua a si mesmo
    if target_user == request.user:
        messages.error(request, 'Você não pode excluir sua própria conta.')
        return redirect('users:admin_users_list')
    
    if request.method == 'POST':
        action = request.POST.get('action', 'deactivate')
        username = target_user.username
        
        if action == 'delete':
            # Hard delete
            ActivityLog.objects.create(
                admin_user=request.user,
                target_user=None,
                action='DELETE_USER',
                role_old=target_user.profile.role if hasattr(target_user, 'profile') else '',
                role_new='',
                ip_address=request.META.get('REMOTE_ADDR')
            )
            target_user.delete()
            messages.success(request, f'Usuário "{username}" excluído permanentemente.')
        else:
            # Soft delete (desativar)
            target_user.is_active = False
            target_user.save()
            ActivityLog.objects.create(
                admin_user=request.user,
                target_user=target_user,
                action='DEACTIVATE_USER',
                role_old=target_user.profile.role if hasattr(target_user, 'profile') else '',
                role_new='',
                ip_address=request.META.get('REMOTE_ADDR')
            )
            messages.success(request, f'Usuário "{username}" desativado com sucesso.')
        
        return redirect('users:admin_users_list')
    
    return render(request, 'users/admin/delete.html', {
        'target_user': target_user,
    })
