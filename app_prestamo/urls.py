from django.urls import path
from .views import inicio, create_task

urlpatterns = [
    path("", inicio),
    path("asd/", create_task, name="create_task"),
]