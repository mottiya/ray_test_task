from celery_config import celery_app
from services.email_service import send_email

send_email_task = celery_app.task(send_email)