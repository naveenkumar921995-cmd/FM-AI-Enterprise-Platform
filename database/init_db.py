from database.db import engine
from database.models import Base

def create_database():
    Base.metadata.create_all(bind=engine)
    print("Database created successfully")

if __name__ == "__main__":
    create_database()