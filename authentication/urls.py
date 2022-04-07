from django.urls import path, include
from rest_framework import routers

from authentication.views import UserViewSet

router = routers.SimpleRouter()
router.register(r"user", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
