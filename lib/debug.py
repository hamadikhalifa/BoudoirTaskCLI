from models import Base, engine


print("Creating all tables...")
Base.metadata.create_all(engine)
print("All tables created successfully.")
