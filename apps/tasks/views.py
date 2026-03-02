from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from apps.users.models import UserProfile

from .forms import TaskForm
from .models import Message, Task, TaskEvidence


def _get_user_profile(user):
    profile, _ = UserProfile.objects.get_or_create(user=user, defaults={"role": "colaborador"})
    return profile


@login_required
def dashboard_view(request):
    user_profile = _get_user_profile(request.user)

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
    task = get_object_or_404(Task, pk=pk)
    messages = task.messages.select_related('sender').all()
    evidences = task.evidences.all()

    return render(request, 'tasks/detail.html', {
        'task': task,
        'messages': messages,
        'evidences': evidences,
    })


@login_required
def edit_task_view(request, pk):
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
    task = get_object_or_404(Task, pk=pk)
    collaborators = User.objects.filter(profile__role='colaborador').order_by('first_name', 'username')

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        if user_id:
            task.assigned_to_id = user_id
            task.status = 'alocada'
            task.save()
        return redirect('tasks:detail', pk=task.pk)

    return render(request, 'tasks/assign.html', {'task': task, 'collaborators': collaborators})


@login_required
def complete_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        description = request.POST.get('description')
        photo = request.FILES.get('photo')

        if photo:
            TaskEvidence.objects.create(task=task, photo=photo, description=description)

        task.status = 'concluida'
        task.save()
        return redirect('tasks:detail', pk=task.pk)

    return render(request, 'tasks/complete.html', {'task': task})


@login_required
def validate_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.status = 'finalizada'
        task.save()

    return redirect('tasks:detail', pk=task.pk)


@login_required
def add_message_view(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        content = (request.POST.get('content') or '').strip()
        if content:
            Message.objects.create(task=task, sender=request.user, content=content)

    return redirect('tasks:detail', pk=task.pk)
