from django.db import models
from django.db.models.deletion import DO_NOTHING, SET_NULL, CASCADE

from config.settings import AUTH_USER_MODEL


class Answer(models.Model):
    ticket = models.ForeignKey(
        "Ticket",
        on_delete=CASCADE,
        null=True,
        blank=True,
        related_name="answers_to_tickets",
    )
    prev_answer = models.ForeignKey("self", on_delete=DO_NOTHING, null=True, blank=True)
    text = models.TextField(blank=False, null=False)

    author = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=SET_NULL, blank=True, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.text}, {self.prev_answer}"


class Ticket(models.Model):
    UNRESOLVED_STATUS = 1
    IN_PROGRESS_STATUS = 2
    RESOLVED_STATUS = 3

    STATUS_CHOICES = (
        (UNRESOLVED_STATUS, "UNRESOLVED"),
        (IN_PROGRESS_STATUS, "IN_PROGRESS"),
        (RESOLVED_STATUS, "RESOLVED"),
    )

    theme = models.CharField(max_length=255, blank=False, null=False)

    body = models.TextField(blank=False, null=False)
    status = models.PositiveSmallIntegerField(
        default=UNRESOLVED_STATUS, choices=STATUS_CHOICES
    )

    reporter = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="ticket_reporter",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.theme
