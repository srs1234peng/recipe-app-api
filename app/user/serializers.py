"""
Serializers for the user API View.
"""
<<<<<<< HEAD
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
=======
from django.contrib.auth.models import ger_user_model
>>>>>>> 2a92dbb4a31e0055fa2ab6340d780f9b3d283e59

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)
    