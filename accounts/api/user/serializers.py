from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings

from rest_framework import serializers

from taskapp.api.serializers import ToDoListInlineSerializer

User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    To_do_list = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri',
            'To_do_list'
        ]
    def get_uri(self, obj):
        return '/api/tasklist/{id}/'.format(id=obj.id)
    def get_To_do_list(self, obj):

        request = self.context.get('request')
        limit = 10
        if request:
            limit_query= request.GET.get('limit')
            try:
                limit = int(limit_query)
            except:
                pass
        qs = obj.todolist_set.all().order_by("-created_timestamp")  # [:10]  # ToDoList.objects.filter(user = obj)
        data = {
            'uri': self.get_uri(obj) + "status/",
            'last':ToDoListInlineSerializer(qs.first()).data,
            'recent': ToDoListInlineSerializer(qs[:limit], many=True).data
        }
        return data