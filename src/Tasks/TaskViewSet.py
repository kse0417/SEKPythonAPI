from rest_framework import viewsets
from .taskSerializer import TaskSerializer
from .task import Task


class TaskViewSet(viewsets.ModelViewSet):
    """
    Django Controller for Task API Endpoint
    ModelViewSet : Includes Create, Update, List, Retrieve, Delete functions
    """

    # ModelViewSet Attributes
    serializer_class = TaskSerializer
    # TODO: Add this - permission_classes = None

    def get_queryset(self):
        """
        Allow users to filter the list view by giving query parameters
        :return:
        """
        queryset = Task.objects.all()
        # TODO: Add all these queries
        #Query by assignee

        #Query by assignGroup

        #Query by Priority
        # priority = self.request.query_params.get("priority", None)
        # if priority is not None:
        #     queryset = queryset.filter()
