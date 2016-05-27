from rest_framework import viewsets
from .taskSerializer import TaskSerializer
from .task import Task


class TaskViewSet(viewsets.ModelViewSet):
    """
    Task API Endpoint
    """

    # ModelViewSet Attributes
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # TODO: Add this - permission_classes = None