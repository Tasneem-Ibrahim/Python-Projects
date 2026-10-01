# Theater_app\src\model\model.py

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

# model.py defines the structure/schema of the Review database table, including its fields, data types, and validation rules.