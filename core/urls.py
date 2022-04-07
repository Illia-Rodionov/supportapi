from django.urls import include, path
from rest_framework import routers
from core.views import (
    AnswerViewSet,
    TicketStatusUpdate,
    TicketViewSet,
)

router = routers.SimpleRouter()
router.register(r"ticket", TicketViewSet)
router.register(r"answer", AnswerViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("status_update/<int:pk>/", TicketStatusUpdate.as_view()),
]
