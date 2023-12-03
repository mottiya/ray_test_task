import pytest
from services.gmail_service import GmailService
from urllib import parse

def test_gmail_service():
    print(parse.parse_qsl('http%3A%2F%2Flocalhost%3A9009%2F'))
    service = GmailService()
    assert service.send_message('teekzaur@gmail.com', 'Test', 'Test message') == True