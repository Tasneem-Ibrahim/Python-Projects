# Theater_app\src\db\engine.py

from sqlmodel import SQLModel, create_engine, Session
import model 


# This code creates the database engine and defines a function to create the required database tables based on the SQLModel models.

database_url = "sqlite:///database.db"
engine = create_engine(database_url, echo=True)


def create_tables():
    SQLModel.metadata.create_all(engine) 
    # # SQLModel.metadata.create_all(engine) creates the required tables if they do not already exist.
    # If a table already exists, it skips that table and does not create it again.


# open/close DB connection ke liye session generator function
def get_session():
    with Session(engine) as session:
        yield session


# engine.py is responsible for setting up the SQLite database connection and managing database sessions.

# create_engine() creates the database engine that manages communication with the SQLite database.

# The database_url specifies which database the application should connect to.

# create_tables() checks the SQLModel models and ensures that the required database tables exist.

# If a table already exists, it is not created again.

# get_session() creates a database session using Session(engine) and provides it to the API routes through yield.

# The with block ensures that the session is automatically closed once the database operations are completed.

# SQLModel, create_engine, and Session are imported from the SQLModel library.

# The model module is also imported so that SQLModel can recognize the application's database models.

