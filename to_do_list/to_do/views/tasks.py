from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404

from to_do.models import Task
from to_do.choice_config import CHOICES


def index_view(request):
    if request.GET.get('pk'):
        to_delete_task_pk = request.GET.get("pk")
        task = Task.objects.get(pk=to_delete_task_pk)
        task.delete()
        print(f'Удалена запись: {task}')
        return redirect(f'/')
    if request.method == 'GET':
        tasks = Task.objects.all()
        context = {
            'tasks': tasks,
        }
        return render(request, 'index.html', context)

def add_task_view(request):
    if request.method == 'GET':
        context = {
            'CHOICES': CHOICES
        }
        return render(request, 'add_task.html', context)
    return added_task_prepare(request)

def added_task_prepare(request):
    if request.POST.get("deadline") == '':
        deadline = None
    else:
        deadline = request.POST.get("deadline")
    task = Task.objects.create(
        task_text=request.POST.get("task_text"),
        task_description=request.POST.get("task_description"),
        state=request.POST.get("state"),
        deadline=deadline
    )
    return redirect(f'/tasks/{task.pk}')

def task_view(request, pk):
    if request.POST.get("task_description") == '':
        task = Task.objects.get(pk=pk)
        task_description = task.task_description
    if request.POST.get("deadline") == '':
        deadline = None
    else:
        deadline = request.POST.get("deadline")
    if request.method == 'POST':
        Task.objects.filter(pk=pk).update(
            task_text=request.POST.get("task_text"),
            task_description=request.POST.get("task_description"),
            state=request.POST.get("state"),
            deadline=deadline
        )
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={'task': task})

def task_edit_view(request, pk):
    task = Task.objects.get(pk=pk)
    context = {
            'CHOICES': CHOICES,
            'task': task,
        }
    return render(request, 'edit_task.html', context)
