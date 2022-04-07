from rest_framework import serializers
from core.models import Answer, Ticket


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)
    ticket = serializers.SlugRelatedField(slug_field="theme", read_only=True)

    class Meta:
        model = Answer
        fields = ("id", "ticket", "prev_answer", "text", "author", "created_at")


class TicketSerializer(serializers.ModelSerializer):
    answers_to_tickets = AnswerSerializer(many=True, read_only=True)
    reporter = serializers.SlugRelatedField(slug_field="username", read_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Ticket
        fields = (
            "id",
            "theme",
            "body",
            "reporter",
            "status",
            "created_at",
            "answers_to_tickets",
        )

    def create(self, validated_data):
        """При создании тикета reporter == user.request"""
        validated_data["reporter"] = self.context["request"].user
        return super().create(validated_data)


class TicketStatusUpdateSerializer(serializers.ModelSerializer):
    reporter = serializers.CharField(read_only=True)
    theme = serializers.CharField(read_only=True)

    class Meta:
        model = Ticket
        fields = ("id", "theme", "status", "reporter")
