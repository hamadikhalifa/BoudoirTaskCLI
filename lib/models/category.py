from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="categories")
    tasks = relationship("Task", back_populates="category", cascade="all, delete")

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}', user_id={self.user_id})>"
