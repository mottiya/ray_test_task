import base64

from email.message import EmailMessage

from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from requests import HTTPError

from singleton_decorator import singleton
from config import GMAIL_HOST, GMAIL_PORT
import os.path
# NOT WORKING


# @singleton
class GmailService():
    SCOPES = [
            "https://www.googleapis.com/auth/gmail.send"
        ]
    def __init__(self) -> None:
        creds = None

        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", GmailService.SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", GmailService.SCOPES
                )
                creds = flow.run_local_server(port=GMAIL_PORT)
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        try:
            self.service = build("gmail", "v1", credentials=creds)
            results = self.service.users().labels().list(userId="me").execute()
            labels = results.get("labels", [])

            if not labels:
                print("No labels found.")
                return
            print("Labels:")
            for label in labels:
                print(label["name"])

        except HttpError as error:
            # TODO(developer) - Handle errors from gmail API.
            print(f"An error occurred: {error}")
    
    def send_message(self, recipient_email:str, title:str, content:str, recipient_username: str | None = None):
        message = EmailMessage()
        message['Subject'] = title
        message['To'] = recipient_email

        if recipient_username is not None:
            try:
                content = content.format(username=recipient_username)
            except KeyError:
                pass
        
        message.set_content(
            content,
            subtype='html'
        )

        create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

        try:
            message = (self.service.users().messages().send(userId="me", body=create_message).execute())
            print(F'sent message to {message} Message Id: {message["id"]}')
        except HTTPError as error:
            print(F'An error occurred: {error}')
            message = None
