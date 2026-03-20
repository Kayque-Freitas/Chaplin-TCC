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

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            profile = getattr(user, 'profile', None)
            if profile and profile.two_factor_enabled and profile.totp_secret:
                # Store user id in session for 2FA step (don't log in yet)
                request.session['pre2fa_user_id'] = user.id
                request.session['pre2fa_user_backend'] = user.backend
                return redirect('users:two_factor_verify')
            login(request, user)
            return redirect('tasks:dashboard')
        else:
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

@login_required
def register_view(request):
    """View para registrar novos usuários (restrito a gestores e admins)"""
    if not is_admin(request.user) and not _is_manager(request.user):
        messages.error(request, 'Sem permissão para criar contas.')
        return redirect('tasks:dashboard')
        
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Form is valid, create user but don't save yet to set password properly
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            # The UserProfile is automatically created via the post_save signal
            # Default role is 'colaborador' which is fine
            
            messages.success(request, f'Usuário {user.username} criado com sucesso!')
            return redirect('users:admin_users_list' if is_admin(request.user) else 'tasks:dashboard')
    else:
        form = UserRegistrationForm()
        
    return render(request, 'users/register.html', {'form': form})

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
