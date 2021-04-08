from django.contrib import admin
from django.conf.urls import url
from django.urls import path

from .views import UserDetailAPIView, UserToDoListAPIView

urlpatterns = [
    url(r'^(?P<username>\w+)/$', UserDetailAPIView.as_view(), name="detail"),
    url(r'^(?P<username>\w+)/todolist/$', UserToDoListAPIView.as_view(), name="ToDoList"),
]