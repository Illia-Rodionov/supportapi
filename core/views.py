from rest_framework import viewsets, generics
from authentication.permissions import IsSupport
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from core.serializers import (
    AnswerSerializer,
    TicketSerializer,
    TicketStatusUpdateSerializer,
)
from core.models import Ticket, Answer, EmailQueue
from core.tasks import status_send_info


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """Return an object for the current authenticated user only"""
        return self.queryset.filter(reporter=self.request.user)


class TicketStatusUpdate(generics.RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketStatusUpdateSerializer
    # permission_classes = [IsSupport, IsAuthenticated]

    def put(self, request, *args, **kwargs):
        email_template = "Your ticket has an updated ticket!"
        ticket_data = self.get_serializer(self.get_queryset().filter(id=kwargs["pk"]).first())
        email = EmailQueue(
            email_queue=ticket_data.data["reporter"]["email"],
            email_text=email_template,
        )
        email.save()
        status_send_info.delay(email.email_queue, email.email_text)
        # email.delete()
        return self.update(request, *args, **kwargs)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
