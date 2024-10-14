from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())])

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password])
    
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', instance.password)

        instance.set_password(password)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance