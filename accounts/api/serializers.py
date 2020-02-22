from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
from accounts.models import User
from rest_framework import serializers

User._meta.get_field('email')._unique = True


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_student', 'is_teacher')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_student', 'is_teacher')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data, **extra_fields):
        extra_fields.setdefault('is_student', False)
        extra_fields.setdefault('is_teacher', False)

        extra_fields['is_student'] = validated_data['is_student']
        extra_fields['is_teacher'] = validated_data['is_teacher']

        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
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
