# Theater_app\main.py

from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from src.db.engine import create_tables
from src.routes.review_route import router as review_router
from src.utils.exception import InvalidReviewError, invalid_review_error_handler

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception class register in fastApi
app.add_exception_handler(InvalidReviewError, invalid_review_error_handler)

app.include_router(review_router) 
# Includes the review router to handle review-related endpoints.
# It adds all review APIs defined in review_route.py to the main FastAPI application.


@app.get("/")
def hello():
    index_path = Path(__file__).parent / "index.html" 
    if index_path.exists():
        return FileResponse(index_path)
    return {"message": "Welcome to the Theater App Backend!"}

# The hello() function handles the GET / request. If index.html is available, it returns the HTML file; otherwise, it returns a welcome message.

# When the application starts, the lifespan() function in main.py manages the application's startup and shutdown processes.

# During startup, it calls create_tables(), which checks the SQLModel models and creates the required tables in the SQLite database if they do not already exist.

# FastAPI() creates the main application.

# add_middleware() configures CORS to allow frontend and backend requests.

# add_exception_handler() handles custom application errors.

# include_router() adds all review APIs defined in review_route.py to the main application.

# hello() handles the GET / request.
