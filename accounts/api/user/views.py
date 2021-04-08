from django.contrib.auth import get_user_model

from .serializers import  UserDetailSerializer
from taskapp.api.serializers import ToDoListInlineSerializer
from taskapp.models import ToDoList
from rest_framework import generics, permissions

from accounts.api.permissions import AnonPermissionOnly
User = get_user_model()

class UserDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = 'username' #id

    def get_serializer_context(self):
        return  {'request': self.request}


class UserToDoListAPIView(generics.ListAPIView):
    serializer_class = ToDoListInlineSerializer
    # pagination_class = customPagination
    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get("username", None)
        if username is None:
            return  ToDoList.objects.none()
        return ToDoList.objects.filter(user__username=username)

