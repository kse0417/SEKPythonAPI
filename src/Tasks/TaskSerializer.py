from rest_framework import serializers
from .task import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('url', 'title', 'description', 'dueDate', 'priority')
