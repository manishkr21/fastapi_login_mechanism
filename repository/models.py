from sqlalchemy import Column, Integer, String, Boolean
from repository.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    disabled = Column(Boolean)

