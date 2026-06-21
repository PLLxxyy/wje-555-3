from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

from apps.auth.backends import create_token
from apps.common.constants import UserRole

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "role", "nickname", "phone", "email", "avatar", "idCardNo", "createdAt"]
        read_only_fields = ["id", "createdAt"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    role = serializers.ChoiceField(choices=[UserRole.LANDLORD, UserRole.TENANT])

    class Meta:
        model = User
        fields = ["id", "username", "password", "role", "nickname", "phone", "email"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(username=attrs["username"], password=attrs["password"])
        if not user:
            raise serializers.ValidationError("用户名或密码错误")
        attrs["user"] = user
        attrs["token"] = create_token(user)
        return attrs

