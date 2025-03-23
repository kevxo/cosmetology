from sqlalchemy import Column, String
from .base import Base

class User(Base):
    __tablename__ = 'users'

    uuid = Column(String(36), primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)