import django_filters
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import mixins
from rest_framework import generics
from .taskSerializer import TaskSerializer
from .task import Task


class TaskFilter(filters.FilterSet):
    date_range = django_filters.DateRangeFilter()

    class Meta:
        model = Task
        fields = ['category', 'priority', 'parent_task', 'date_range']


class TaskListView(generics.ListAPIView):
    """
    Task API Endpoint
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = TaskFilter


class TaskViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    """
    Task API Endpoint
    """

    # ModelViewSet Attributes
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # TODO: Add this - permission_classes = None
