from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from datetime import timedelta

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    refresh['username'] = user.username
    refresh['access']= str(refresh.access_token)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

User = get_user_model()
expire_delta = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']




class UserPublicSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri'
        ]
    def get_uri(self, obj):
        return '/api/tasklist/{id}'.format(id=obj.id)


class UserRegisterSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    expires = serializers.SerializerMethodField(read_only=True)
    message = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'token',
            'expires',
            'message'
            ]
        extra_kwargs = {'password' : {'write_only': True}}

    def validate_email(self, value):
        qs =  User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("User with this email already exists")
        return value

    def validate_username(self, value):
        qs =  User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("User with this username already exists")
        return value

    def get_message(self, obj):
        return "Thank you for registering, please verify mail before continuing"

    def get_token(self, obj): #instance of the model that is working with the serializer
        user = obj
        token = get_tokens_for_user(user)
        return token

    def get_expires(self, obj):
        return timezone.now() + expire_delta - timedelta(seconds=200)


    def validate(self, data):
        pw = data.get('password')
        pw2 = data.pop('password2')
        if(pw != pw2):
            raise serializers.ValidationError("passwords must match")
        return data

    def create(self, validated_data):
        # print(validated_data)
        user_obj = User(
                username=validated_data.get('username'),
                email=validated_data.get('email'))
        user_obj.set_password(validated_data.get('password'))
        user_obj.is_active= False
        user_obj.save()
        return user_obj