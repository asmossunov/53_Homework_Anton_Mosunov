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
    task = Task.objects.create(
        task_text=request.POST.get("task_text"),
        deadline=request.POST.get("deadline"),
        state=request.POST.get("state")
    )
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'index.html', context)


