from django.contrib.auth.models import User, Group
from rest_framework import serializers

from loteria.app.models import MegaSena


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MegaSena
        fields = '__all__'
