from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, String, TIMESTAMP

from database import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    username: str = Column(String, nullable=False)
    registred_at: int = Column(TIMESTAMP, default=datetime.utcnow)