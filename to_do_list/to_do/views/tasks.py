from datetime import datetime
from django.shortcuts import render

from to_do.models import Task
from to_do.choice_config import CHOICES


def index_view(request):
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
    print(task)
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'index.html', context)


def task_view(request):
    pk = request.GET.get('pk')
    task = Task.objects.get(pk=pk)
    return render(request, 'task.html', context={'task': task})
