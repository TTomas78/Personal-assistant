from models import BaseModel

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

class UserModel(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    nickname = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    