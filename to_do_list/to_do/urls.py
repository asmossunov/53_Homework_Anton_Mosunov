from django.contrib import admin
from django.urls import path

from to_do.views.tasks import index_view, add_task_view, task_view, task_edit_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('tasks/add/', add_task_view),
    path('tasks/<int:pk>', task_view),
    path('edit/', task_view),
    path('tasks/edit/<int:pk>', task_edit_view)
]
