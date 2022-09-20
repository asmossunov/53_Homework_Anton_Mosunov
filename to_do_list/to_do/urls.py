from django.contrib import admin
from django.urls import path

from to_do.views.tasks import index_view, add_task_view, task_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('add_task/', add_task_view),
    path('tasks/', task_view)
]
