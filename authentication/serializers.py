from rest_framework import serializers
from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "role", "created_at", "password")
