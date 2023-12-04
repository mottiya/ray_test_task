from datetime import datetime
import uuid

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, For


from database import Base

class NewsLetter(Base):
    __tablename__ = "newsletter"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    owner_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"))
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))

class Post(Base):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(primary_key=True)

