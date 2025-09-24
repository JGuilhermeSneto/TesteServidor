from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Task
from .forms import TaskForm

@login_required
def dashboard(request):
    if request.user.is_staff:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(assigned_to=request.user)
    
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    return render(request, 'core/dashboard.html', {'tasks': tasks, 'form': form})


@login_required
def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.user.is_staff or task.assigned_to == request.user:
        task.status = 'C' if task.status == 'P' else 'P'
        task.save()
    return redirect('dashboard')


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})
