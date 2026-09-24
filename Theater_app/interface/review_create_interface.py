# Theater_app\interface\review_create_interface.py
from sqlmodel import SQLModel, Field


# #  Validation class ( request body validation ) for creating a new review
class ReviewCreate(SQLModel):
    play_name: str
    reviewer_name: str
    rating: int = Field(ge=1, le=5)  # Rating between 1 and 5
    comment: str