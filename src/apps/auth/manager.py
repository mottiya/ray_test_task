from typing import Optional
import uuid

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin, exceptions, models, schemas

from .models import User
from .utils import get_user_db
from .tasks import send_email_task
from .tamplates import email_verifi_tamplate
from config import SECRET_RESET_PWD, SECRET_VERIVY_EMAIL
from consts import APP_NAME



class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET_RESET_PWD
    verification_token_secret = SECRET_VERIVY_EMAIL

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")
    
    async def on_after_verify(
        self, user: User, request: Optional[Request] = None
    ):
        print(f"User {user.id} has been verified")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")
    
    async def on_after_reset_password(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has reset their password.")

    
async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)