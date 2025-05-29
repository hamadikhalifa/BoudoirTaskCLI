from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    category = relationship("Category", back_populates="tasks")
    user = relationship("User", back_populates="tasks")

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', category_id={self.category_id}, user_id={self.user_id})>"
