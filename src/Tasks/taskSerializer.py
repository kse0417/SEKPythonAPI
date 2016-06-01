from rest_framework import serializers
from .task import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'category', 'due_date', 'priority', 'parent_task')
