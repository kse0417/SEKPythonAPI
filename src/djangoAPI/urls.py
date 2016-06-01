from django.conf.urls import url, include
from rest_framework import routers
from src.tasks import taskViewSet
from src.users import groupViewSet

router = routers.DefaultRouter()
router.register(r'tasks', taskViewSet.TaskViewSet, 'tasks')
router.register(r'groups', groupViewSet.GroupViewSet, 'groups')
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^tasks/', taskViewSet.TaskListView.as_view()),
    url(r'^groups/', groupViewSet.GroupListView.as_view()),
    url(r'^', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls'))
]
