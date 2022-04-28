import django
from django.core.mail import send_mail

from config import settings
from core.models import EmailQueue

django.setup()
from config.celery import app
from core.send_mail import send

gmail_user = settings.EMAIL_HOST_USER
gmail_password = settings.EMAIL_HOST_PASSWORD


@app.task
def status_send_info(email_queue=None, email_text=None):
    send(email_queue, email_text)


@app.task
def schedule_send():
    for email in EmailQueue.objects.all():
        send_mail(subject=email.email_text,
                  message=email.email_text,
                  from_email=gmail_user,
                  recipient_list=[email.email_queue],
                  fail_silently=False,
                  auth_user=gmail_user,
                  auth_password=gmail_password
        )