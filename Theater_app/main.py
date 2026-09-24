# Theater_app\main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI
from engine import create_tables
from routes.review_route import router

#  control your starting and ending of server
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run before the application starts
    print("✔ Starting the Theater App Backend...")
    create_tables()  # Ensure tables are created before the app starts
    yield
    # Code to run after the application stops
    print("🔒 Shutting down the Theater App Backend...")


app = FastAPI(
    title="Theater App Backend",
    description="This is the backend for the Theater App, which provides APIs for managing theater performances, tickets, and user interactions.",
    lifespan=lifespan
)

app.include_router(router, tags=["Reviews"])

@app.get("/")
def hello():
    return {"message": "Welcome to the Theater App Backend!"}

