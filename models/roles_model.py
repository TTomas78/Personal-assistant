from pickle import TRUE
from models import BaseModel
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

class RolesModel(BaseModel):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(255), nullable=False)

