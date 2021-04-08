import json
from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
# from django.views.generic import View
from accounts.api.permissions import IsOwnerOrReadOnly
from taskapp.models import ToDoList
from .serializers import ToDoListSerializer
from django.shortcuts import get_object_or_404



def is_json(data):
    try:
        json_data = json.loads(data)
        is_valid = True
    except:
        is_valid = False
    return is_valid


class ToDoListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        qs = ToDoList.objects.all()
        print(qs)
        serialized_data = ToDoListSerializer(qs, many=True)
        return Response(serialized_data.data)

    def post(self, request, format=None):
        qs = ToDoList.objects.all()
        print(qs)
        serialized_data = ToDoListSerializer(qs, many=True)
        return Response(serialized_data.data)


# CreateModelMixin -- POST method
# UpdateModelMixin -- PUT method
# DestroyModelMixin -- DELETE method
class ToDoAPIView(
    mixins.CreateModelMixin,
    generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ToDoListSerializer
    # filter_fields = {'priority':['startswith']}
    filter_fields = ('name', 'priority', 'modified_timestamp', 'created_timestamp')
    search_fields = ('name', 'priority')
    ordering_fields = ('priority','modified_timestamp','created_timestamp')
    queryset = ToDoList.objects.all()
    # passed_id = None
    # def get_queryset(self):
    #     qs = ToDoList.objects.all()
    #     query = self.request.GET.get('q')
    #     # print(query)
    #     print(self.request.user)
    #     if query is not None:
    #         qs = qs.filter(name__icontains=query)
    #     return qs

    # def get_object(self):
    #     request = self.request
    #     passed_id = request.GET.get('id', None)  or self.passed_id
    #     queryset = self.get_queryset()
    #     obj = None
    #     # print("here",passed_id)
    #     if(passed_id is not None):
    #         obj = get_object_or_404(queryset, id = passed_id)
    #         self.check_object_permissions(request, obj)
    #     return obj
    #
    # def get(self, request, *args, **kwargs):
    #     url_passed_id = request.GET.get('id', None)
    #     body_ = request.body
    #     json_data= {}
    #     if(is_json(body_)):
    #         json_data = json.loads(request.body)
    #     new_passed_id = json_data.get('id', None)
    #     passed_id = url_passed_id or new_passed_id or None
    #     self.passed_id = passed_id
    #     print(request.body)
    #     if(passed_id is not None):
    #         return self.retrieve(request, *args, **kwargs)
    #
    #     return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     url_passed_id = request.GET.get('id', None)
    #     body_ = request.body
    #     json_data = {}
    #     if (is_json(body_)):
    #         json_data = json.loads(request.body)
    #     new_passed_id = json_data.get('id', None)
    #     passed_id = url_passed_id or new_passed_id or None
    #     self.passed_id = passed_id
    #     return self.update(request, *args, **kwargs)
    #
    # def patch(self, request, *args, **kwargs):
    #     url_passed_id = request.GET.get('id', None)
    #     body_ = request.body
    #     json_data = {}
    #     if (is_json(body_)):
    #         json_data = json.loads(request.body)
    #     new_passed_id = json_data.get('id', None)
    #     passed_id = url_passed_id or new_passed_id or None
    #     self.passed_id = passed_id
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     url_passed_id = request.GET.get('id', None)
    #     body_ = request.body
    #     json_data = {}
    #     if (is_json(body_)):
    #         json_data = json.loads(request.body)
    #     new_passed_id = json_data.get('id', None)
    #     passed_id = url_passed_id or new_passed_id or None
    #     #print(passed_id)
    #     self.passed_id = passed_id
    #     return self.destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# class ToDoCreateAPIView(generics.CreateAPIView):
#     permission_classes     = []
#     authentication_classes = []
#     queryset  = ToDoList.objects.all()
#     serializer_class = ToDoListSerializer

# def perform_create(self, serializer):
#     serializer.save(user=self.request.user)

class ToDoDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)



# class ToDoUpdateAPIView(generics.UpdateAPIView):
#     permission_classes     = []
#     authentication_classes = []
#     queryset  = ToDoList.objects.all()
#     serializer_class = ToDoListSerializer

# class ToDoDeleteAPIView(generics.DestroyAPIView):
#     permission_classes     = []
#     authentication_classes = []
#     queryset  = ToDoList.objects.all()
#     serializer_class = ToDoListSerializer



# List items view

from .serializers import ListItemSerializer
from taskapp.models import ListItem
class ListAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_fields = ('item_name', 'priority', 'modified_timestamp', 'created_timestamp')
    search_fields = ('item_name', 'priority')
    ordering_fields = ('priority', 'modified_timestamp', 'created_timestamp')
    
    serializer_class = ListItemSerializer
    queryset = ListItem.objects.all()
    # def get(self, request):
    #     start = request.GET.get('start', None)
    #     end = request.GET.get('end', None)
    #     return Response(ListItem.objects.filter(created_timestamp__range=(start, end)))

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class ListDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


#Fetch Weather Data
import requests
from django.views.generic import DetailView
from django.http import JsonResponse
class Weather(DetailView):
    permission_classes = [permissions.IsAuthenticated]

    # city = 'Las Vegas'

    def get(self, request, *args, **kwargs):
        url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=de9471a428fc468c16c7590e4ec77409'
        latitude = request.GET.get('lat', None)
        longitude = request.GET.get('lon', None)
        print(latitude, longitude)
        # latitude = 17.3850
        # longitude = 78.4867
        location_temp = requests.get(url.format(latitude, longitude)).json()
        if(latitude==None and longitude ==None):
            return JsonResponse({'query': 'provide query params lat and long'})
        weather = {
            'humidity': location_temp['main']['humidity'],
            'temperature': location_temp['main']['temp'],
            'description': location_temp['weather'][0]['description'],
            'icon': location_temp['weather'][0]['icon']
        }

        return JsonResponse(weather)
    # lookup_field = 'id'



