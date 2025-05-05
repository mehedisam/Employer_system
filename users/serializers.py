from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class SignUpSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""
    class Meta:
        model = User
        fields = ("id", "email", "password")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    """Serializer for user profile display."""
    class Meta:
        model = User
        fields = ("id", "email", "is_active", "date_joined")
        read_only_fields = ("is_active", "date_joined")
