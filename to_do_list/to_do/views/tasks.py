from django.shortcuts import render

from to_do.models import Task


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
    return render(request, 'add_task.html')


def added_task_prepare(request):
    task = Task.objects.create(
        task_text=request.POST.get("task_text"),
        deadline=request.POST.get("deadline")
    )
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'index.html', context)


