
from config import settings

from config.celery import app
from core.send_mail import send

gmail_user = settings.EMAIL_HOST_USER
gmail_password = settings.EMAIL_HOST_PASSWORD


@app.task
def status_send_info(email_queue=None, email_text=None):
    send(email_queue, email_text)

