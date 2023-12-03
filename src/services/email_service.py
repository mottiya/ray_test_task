import smtplib
from email.message import EmailMessage
import ssl

from config import SMTP_HOST, SMTP_PORT, EMAIL_ADRESS, EMAIL_SECRET
# NOT WORKING

def get_email_template(email_reciever:str, title:str, content:str, username: str | None = None):
    email = EmailMessage()
    email['Subject'] = title
    email['From'] = EMAIL_ADRESS
    email['To'] = email_reciever

    if username is not None:
        try:
            content = content.format(username=username)
        except KeyError:
            pass
    
    email.set_content(
        content,
        subtype='html'
    )
    return email

def send_email(email_reciever:str, title:str, content:str, username: str | None = None) -> bool:
    message = get_email_template(email_reciever, title, content, username)
    try:
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=ssl.create_default_context()) as server:
            server.login(EMAIL_ADRESS, EMAIL_SECRET)
            server.send_message(message, sender=EMAIL_ADRESS)
        return True
    except smtplib.SMTPException:
        print("SMTP some exception")
        return False