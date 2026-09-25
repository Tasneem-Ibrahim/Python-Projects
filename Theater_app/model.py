# Theater_app\model.py

from sqlmodel import Field, SQLModel, create_engine
from typing import Optional
from datetime import datetime, timezone

# Table structure (Schema) for the Review model
class Review(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    play_name: str = Field(index=True)
    reviewer_name: str
    rating: int = Field(ge=1, le=5)  # Rating between 1 and 5
    comment: str
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )



# #  Respnse Body Structure
# class ReviewRead(SQLModel):
#     id: int
#     play_name: str
#     reviewer_name: str
#     rating: int
#     comment: str
#     created_at: datetime

# class ReviewUpdate(SQLModel):
#     play_name: Optional[str] = None
#     reviewer_name: Optional[str] = None
#     rating: Optional[int] = Field(default=None, ge=1, le=5)
#     comment: Optional[str] = None



