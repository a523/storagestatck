from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)
        read_only_fields = ('is_superuser', 'last_login')
