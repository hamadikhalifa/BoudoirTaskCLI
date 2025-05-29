from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)


    categories = relationship("Category", back_populates="user", cascade="all, delete")
    tasks = relationship("Task", back_populates="user", cascade="all, delete")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"
