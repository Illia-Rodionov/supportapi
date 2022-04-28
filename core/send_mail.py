from core.models import EmailQueue
from config import settings

from django.core.mail import send_mail

gmail_user = settings.EMAIL_HOST_USER
gmail_password = settings.EMAIL_HOST_PASSWORD



def send(email_queue, email_text):
    send_mail(subject=email_text,
              message=email_text,
              from_email=gmail_user,
              recipient_list=[email_queue],
              fail_silently=False,
              auth_user=gmail_user,
              auth_password=gmail_password

    )



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