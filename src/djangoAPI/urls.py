from django.conf.urls import url, include
from rest_framework import routers
from src.tasks import taskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', taskViewSet.TaskViewSet, 'tasks')
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls'))
]
