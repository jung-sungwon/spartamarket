from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserCreateSerializer(UserSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password", "name", "nickname", "birthday")
        extra_kwargs = {
            "password": {"write_only": True},
            "name": {"required": True},
            "nickname": {"required": True},
            "birthday": {"required": True},
            "email": {"required": True},
            "username": {"required": True},
        }

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
            name=validated_data.get("name", ""),
            nickname=validated_data.get("nickname", ""),
            birthday=validated_data.get("birthday", None),
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
