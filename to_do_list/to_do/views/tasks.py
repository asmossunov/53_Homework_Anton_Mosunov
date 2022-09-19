from django.shortcuts import render

from to_do.models import Task


def index_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'index.html', context)
