from django.contrib import admin
from django.urls import path

from to_do.views.tasks import index_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view)
]
