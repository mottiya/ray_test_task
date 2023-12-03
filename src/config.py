from dotenv import load_dotenv
import os

load_dotenv()

SECRET_AUTH = os.environ.get("SECRET_AUTH")
SECRET_RESET_PWD = os.environ.get("SECRET_RESET_PWD")
SECRET_VERIVY_EMAIL = os.environ.get("SECRET_VERIVY_EMAIL")

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = int(os.environ.get("DB_PORT"))
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

EMAIL_ADRESS = os.environ.get("EMAIL_ADRESS")
EMAIL_SECRET = os.environ.get("EMAIL_SECRET")

SMTP_HOST = os.environ.get("SMTP_HOST")
SMTP_PORT = int(os.environ.get("SMTP_PORT"))

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = int(os.environ.get("REDIS_PORT"))

GMAIL_HOST = os.environ.get("GMAIL_HOST")
GMAIL_PORT = int(os.environ.get("GMAIL_PORT"))