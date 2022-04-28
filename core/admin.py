from django.contrib import admin

from core.models import Answer, Ticket, EmailQueue


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass


@admin.register(EmailQueue)
class EmailQueueAdmin(admin.ModelAdmin):
    pass
