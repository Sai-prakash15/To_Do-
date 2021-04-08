from django.contrib import admin
from django.urls import path, include
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import AuthAPIView, RegisterAPIView

from django.conf.urls import url
urlpatterns = [
    path('', AuthAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('jwt/', MyTokenObtainPairView.as_view()),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]