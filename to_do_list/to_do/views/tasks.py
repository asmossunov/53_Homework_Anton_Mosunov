from datetime import datetime
from django.shortcuts import render, redirect

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
    else:
        return added_task_prepare(request)


def add_task_view(request):
    context = {
        'CHOICES': CHOICES
    }
    return render(request, 'add_task.html', context)


def added_task_prepare(request):
    print(request.POST)
    if request.POST.get("deadline") == '':
        deadline = None
    else:
        deadline = request.POST.get("deadline")
    task = Task.objects.create(
        task_text=request.POST.get("task_text"),
        state=request.POST.get("state"),
        deadline=deadline
    )
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return redirect(f'/tasks/?pk={task.pk}')


def task_view(request):
    pk = request.GET.get('pk')
    task = Task.objects.get(pk=pk)
    return render(request, 'task.html', context={'task': task})

