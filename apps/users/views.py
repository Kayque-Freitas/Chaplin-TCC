from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tasks:dashboard')
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('core:index')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        
        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {'error': 'Usuário já existe'})
        
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name)
        UserProfile.objects.create(user=user, role='colaborador')
        login(request, user)
        return redirect('tasks:dashboard')
    
    return render(request, 'users/register.html')

@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'users/profile.html', {'profile': profile})
