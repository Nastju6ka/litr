from sqlalchemy import Column, Integer, String
from .db import Base


class Users(Base):

    __tablename__ = 'portfolio'

    id = Column(Integer, unique=True, index=True, primary_key=True)
    image = Column(String)
    title = Column(String)
    description = Column(String)
    type = Column(String)

