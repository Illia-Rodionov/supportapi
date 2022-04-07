from rest_framework import viewsets, generics
from authentication.permissions import IsSupport
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from core.serializers import (
    AnswerSerializer,
    TicketSerializer,
    TicketStatusUpdateSerializer,
)
from core.models import Ticket, Answer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    def get_queryset(self):
        """Возвращать объект только для текущего аутентифицированного пользователя"""
        return self.queryset.filter(reporter=self.request.user)


class TicketStatusUpdate(generics.RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketStatusUpdateSerializer
    permission_classes = [IsSupport, IsAuthenticated]


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
