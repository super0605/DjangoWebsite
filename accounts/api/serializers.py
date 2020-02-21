from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
from accounts.models import User
from rest_framework import serializers

User._meta.get_field('email')._unique = True


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_student')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data, **extra_fields):
        extra_fields.setdefault('is_student', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_teacher', False)

        if validated_data['userRole'] is None:
            extra_fields[validated_data['userRole']] = True


        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
            validated_data['is_student'],
            **extra_fields
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
