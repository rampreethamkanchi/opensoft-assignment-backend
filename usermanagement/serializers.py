from rest_framework import serializers
from .models import user
class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['username', 'password', 'email']
class username_serializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['username']
class email_password_serializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['email', 'password']