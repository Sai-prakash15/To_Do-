from datetime import timedelta
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings
from django.utils import timezone
import json
from django.core.serializers.json import DjangoJSONEncoder

from .permissions import AnonPermissionOnly

expire_delta = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print(timezone.now() + expire_delta - timedelta(seconds=200))
        token = super().get_token(user)
        # print("sdv",token)
        # print("I'm here", user.username)
        # Add custom claims
        token['name'] = user.username
        token['expires'] = json.dumps(timezone.now() + expire_delta - timedelta(seconds=200), cls=DjangoJSONEncoder)

        # ...
        # print("token",token)
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
User = get_user_model()

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    refresh['username'] = user.username
    refresh['access']= str(refresh.access_token)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class AuthAPIView(APIView):

    permission_classes = [AnonPermissionOnly]
    def post(self, request, *args, **kwargs):
        # print(request.user)
        if(request.user.is_authenticated):
            return Response({'detail':'You are already authenticated'}, status=400)
        data = request.data
        username = data.get('username')
        password = data.get('password')
        # user = authenticate(username=username, password=password)
        qs = User.objects.filter(
            Q(username__iexact= username) |
            Q(email__iexact=username)
            ).distinct()

        if(qs.count() ==1):
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
                # token = get_tokens_for_user(user)['access']
                token = get_tokens_for_user(user)
                # print(token)
        #print(response)
        #token = get_tokens_for_user(user)['access']
        # print(user)
        #         payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms='HS256')
        #         print("pay",payload)
                return Response(token)
        return Response({"Detail":"Invalid Credentials"}, status=401)


# REGISTER

# class RegisterAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#     def post(self, request, *args, **kwargs):
#         # print(request.user)
#         # print("dsnjfk")
#         if(request.user.is_authenticated):
#             return Response({'detail':'You are already registered or authenticated'}, status=400)
#         data = request.data
#         username = data.get('username')
#         email = data.get('email')
#         password = data.get('password')
#         password2 = data.get('password2')
#         # print("hello")
#         qs = User.objects.filter(
#             Q(username__iexact= username) |
#             Q(email__iexact=username)
#             )
#         # print(qs)
#         if(password != password2):
#             return Response({'detail': 'Passwords must match '}, status=401)
#
#         if(qs.exists()):
#             return Response({'detail': 'You\'ve already registered '}, status=401)
#         else:
#             print("djkvn")
#             user = User.objects.create(username=username, email=email)
#             user.set_password(password)
#             user.save()
#             # token = get_tokens_for_user(user)['access']
#             # payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms='HS256')
#             #         print("pay",payload)
#             return Response({"details":"Thank you for registering, verify your email"}, status=201)

        # return Response({"Detail":"Invalid Request"}, status=401) # does not reach anyway


#REGISTER using serializer

from .serializers import UserRegisterSerializer
from rest_framework import generics

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AnonPermissionOnly]




