from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import *


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, validators=[UniqueValidator(queryset=User.objects.all())])
    phone_number = serializers.CharField(max_length=50, validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'phone_number')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'phone_number', 'password')

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
