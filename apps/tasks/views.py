from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Task, TaskEvidence, Message
from .forms import TaskForm
from apps.users.models import UserProfile

@login_required
def dashboard_view(request):
    """View do dashboard com estatísticas"""
    if not hasattr(request.user, 'profile'):
        UserProfile.objects.create(user=request.user, role='admin' if request.user.is_superuser else 'colaborador')
    user_profile = request.user.profile
    
    if user_profile.role == 'gestor':
        tasks = Task.objects.filter(created_by=request.user)
    elif user_profile.role == 'lider':
        tasks = Task.objects.filter(status__in=['aberta', 'alocada'])
    elif user_profile.role == 'colaborador':
        tasks = Task.objects.filter(assigned_to=request.user)
    else:
        tasks = Task.objects.all()
    
    context = {
        'tasks': tasks,
        'total_tasks': tasks.count(),
        'open_tasks': tasks.filter(status='aberta').count(),
        'assigned_tasks': tasks.filter(status='alocada').count(),
        'completed_tasks': tasks.filter(status__in=['concluida', 'finalizada']).count(),
    }
    return render(request, 'tasks/dashboard.html', context)

@login_required
def tasks_list_view(request):
    """View da lista de tarefas com filtros"""
    status = request.GET.get('status', '')
    priority = request.GET.get('priority', '')
    
    tasks = Task.objects.all()
    
    if status:
        tasks = tasks.filter(status=status)
    if priority:
        tasks = tasks.filter(priority=priority)
    
    return render(request, 'tasks/list.html', {'tasks': tasks})

@login_required
def create_task_view(request):
    """View para criar nova tarefa"""
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('tasks:detail', pk=task.pk)
    else:
        form = TaskForm()
    
    return render(request, 'tasks/create.html', {'form': form})

@login_required
def task_detail_view(request, pk):
    """View do detalhe da tarefa"""
    task = get_object_or_404(Task, pk=pk)
    messages = task.messages.all()
    evidences = task.evidences.all()
    
    return render(request, 'tasks/detail.html', {
        'task': task,
        'messages': messages,
        'evidences': evidences,
    })

@login_required
def edit_task_view(request, pk):
    """View para editar tarefa"""
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/edit.html', {'form': form, 'task': task})

@login_required
def assign_task_view(request, pk):
    """View para alocar tarefa a um usuário"""
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        task.assigned_to_id = user_id
        task.status = 'alocada'
        task.save()
        return redirect('tasks:detail', pk=task.pk)
    
    return render(request, 'tasks/assign.html', {'task': task})

@login_required
def complete_task_view(request, pk):
    """View para marcar tarefa como concluída"""
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        description = request.POST.get('description')
        photo = request.FILES.get('photo')
        
        if photo:
            evidence = TaskEvidence.objects.create(task=task, photo=photo, description=description)
        
        task.status = 'concluida'
        task.save()
        return redirect('tasks:detail', pk=task.pk)
    
    return render(request, 'tasks/complete.html', {'task': task})

@login_required
def add_message_view(request, pk):
    """View para adicionar mensagem/comentário"""
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        content = request.POST.get('content')
        Message.objects.create(task=task, sender=request.user, content=content)
        return redirect('tasks:detail', pk=task.pk)
    
    return render(request, 'tasks/message.html', {'task': task})

@login_required
def settings_view(request):
    """View de configurações do usuário"""
    if not hasattr(request.user, 'profile'):
        UserProfile.objects.create(user=request.user, role='admin' if request.user.is_superuser else 'colaborador')
    user_profile = request.user.profile
    
    if request.method == 'POST':
        # Atualizar configurações
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        
        return redirect('tasks:settings')
    
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'tasks/settings.html', context)
