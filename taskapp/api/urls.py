from django.conf.urls import url
from django.urls import path
from .views import (
    ToDoListSearchAPIView,
    ToDoAPIView,
    # ToDoCreateAPIView,
     ToDoDetailAPIView,
    # ToDoUpdateAPIView,
    # ToDoDeleteAPIView,
    #List item views
    ListAPIView,
    ListDetailAPIView,
    Weather
    )
urlpatterns = [
    #url(r'^$', ToDoListSearchAPIView.as_view()),
    url(r'^$', ToDoAPIView.as_view()),
    # url(r'^create/$', ToDoCreateAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', ToDoDetailAPIView.as_view()),
    # url(r'^(?P<pk>\d+)/update/$', ToDoUpdateAPIView.as_view()),
    # url(r'^(?P<pk>\d+)/delete/$', ToDoDeleteAPIView.as_view()),

    #List item views
    url(r'^list/$', ListAPIView.as_view()),
    url(r'^list/(?P<id>\d+)/$', ListDetailAPIView.as_view()),
    url(r'^weather/$', Weather.as_view()),

]