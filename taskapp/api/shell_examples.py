import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from taskapp.api.serializers import ToDoListSerializer
from taskapp.models import ToDoList

'''
Serializing single object
'''
obj = ToDoList.objects.first()
serializer = ToDoListSerializer(obj)
serializer.data
json_data = JSONRenderer().render(serializer.data)
print(json_data)

stream = io.BytesIO(json_data)
data = JSONParser().parse(stream)
print(data)
'''
Serializing a queryset
'''
qs = ToDoList.objects.all()
serializer2 = ToDoListSerializer(qs, many=True)
serializer2.data
json_data2 = JSONRenderer().render(serializer2.data)
print(json_data2)

stream2 = io.BytesIO(json_data)
data2 = JSONParser().parse(stream)
print(data2)

'''
Create obj
'''

data = {'user': 1}
serializer = ToDoListSerializer(data=data)
serializer.is_valid()
serializer.save()
'''
Update obj
'''
obj = ToDoList.objects.all()[2]
data = {'name': "newList", 'user': 1}
update_serializer = ToDoListSerializer(obj, data=data)
update_serializer.is_valid()
update_serializer.save()


'''
Delete obj
'''

data = {'name': "newList", 'user': 1}
create_serializer = ToDoListSerializer(data=data)
create_serializer.is_valid()
create_obj = create_serializer.save()
print(create_obj)

obj = ToDoList.objects.all()[-1]
delete_serializer = ToDoListSerializer(obj)
print(obj.delete())
