from rest_framework import serializers
from .group import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
