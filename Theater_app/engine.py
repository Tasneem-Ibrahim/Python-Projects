# Theater_app\engine.py
from sqlmodel import SQLModel, create_engine, Session
import model 


# Ye code database engine banata hai aur aapke SQLModel models ke according tables create karne ke liye function define karta hai.

database_url = "sqlite:///database.db"
engine = create_engine(database_url, echo=True)


def create_tables():
    SQLModel.metadata.create_all(engine) 
    # SQLModel.metadata.create_all(engine) existing table ko dobara create nahi karta; agar table already exist ho to usay skip kar deta hai.

# open/close DB connection ke liye session generator function
def get_session():
    with Session(engine) as session:
        yield session

