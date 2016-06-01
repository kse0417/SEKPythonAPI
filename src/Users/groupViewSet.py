import django_filters
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import mixins
from rest_framework import generics
from .groupSerializer import GroupSerializer
from .group import Group


class GroupFilter(filters.FilterSet):
    class Meta:
        model = Group
        fields = ['title']


class GroupListView(generics.ListAPIView):
    """
    Group API Endpoint
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = GroupFilter


class GroupViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    """
    Group API Endpoint
    """

    # ModelViewSet Attributes
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # TODO: Add this - permission_classes = None