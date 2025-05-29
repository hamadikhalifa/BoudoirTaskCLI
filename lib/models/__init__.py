from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///boudoirtaskcli.db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a configured "Session" class
SessionLocal = sessionmaker(bind=engine)

# Base class for declarative models
Base = declarative_base()

# Import your models so they are registered with Base
from .user import User
from .category import Category
from .task import Task

# Expose these symbols when importing * from this package
__all__ = ["User", "Category", "Task", "engine", "SessionLocal", "Base"]
