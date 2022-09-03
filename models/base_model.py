from operator import truediv


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Boolean

class BaseModel(declarative_base()):
    __abstract__ = True

    is_active = Column(Boolean(), default=True, nullable=False, server_default='1')
    is_deleted = Column(Boolean(), default=False, nullable=False, server_default='0')