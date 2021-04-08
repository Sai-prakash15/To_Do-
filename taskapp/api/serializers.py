from rest_framework import serializers

from accounts.api.serializers import UserPublicSerializer
from taskapp.models import ToDoList, ListItem

'''
serializer -> JSON
serializer -> Validate data
'''

class ToDoListInlineSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ToDoList
        fields =[
            'id',
            'name',
            'priority',
            'uri'
        ]

    def get_uri(self, obj):
        return "/api/taskapp/{id}".format(id=obj.id)

class ToDoListSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ToDoList
        fields =[
            'id',
            'user',
            'name',
            'priority',
            'uri',
        ]
        read_only_fields = ['user']

    def get_uri(self, obj):
        return "/api/taskapp/{id}".format(id=obj.id)

    def validate_name(self,value):
        if(len(value)>250):
            raise serializers.ValidationError("This is long for a list name")
        return value
    def validate(self, data):
        name = data.get("name", None)
        if name == "":
            name=None
        if name is None:
            raise serializers.ValidationError("name is required")
        return data


# class ToDoListNameSerializer(serializers.ModelSerializer):
#     # user = UserPublicSerializer(read_only=True)
#     # uri = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = ToDoList
#         fields =[
#             'name'
#         ]


# List items serializers
class ListItemSerializer(serializers.ModelSerializer):
    # uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ListItem
        fields =[
            'id',
            'to_do_list',
            'item_name',
            'priority',
            # 'uri',
        ]
        # read_only_fields = ['user']

    # def get_uri(self, obj):
    #     return "/api/taskapp/{id}".format(id=obj.id)

    def validated_todolist(self, value):
        if(value not in ToDoList.objects.values_list('name', flat=True)):
            raise serializers.ValidationError("List name is not yet created, please create the list first")
        return value

    def validate_name(self,value):
        if(len(value)>100):
            raise serializers.ValidationError("This is long for a list name")
        return value
    def validate(self, data):
        item_name = data.get("item_name", None)
        if item_name == "":
            item_name=None
        if item_name is None:
            raise serializers.ValidationError("name is required")
        return data
