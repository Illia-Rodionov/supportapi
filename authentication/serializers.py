from rest_framework import serializers
from authentication.models import User




class UserCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password")


class UserDetailSerializer(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ("email", "role", "created_at")
