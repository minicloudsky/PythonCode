from django.conf.urls import url, include
from rest_framework import routers
from passage import views

router = routers.DefaultRouter()
router.register(r'passages', views.PassageViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'api-passage/', include('rest_framework.urls', namespace='rest_framework')),
]
