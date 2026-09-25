# Theater_app\routes\review_route.py
from fastapi import APIRouter, Depends
from sqlmodel import Session
from engine import get_session
from interface.review_create_interface import ReviewCreate
from model import Review
import rich


router = APIRouter(prefix="/review")

# POST localhost:8000/review

@router.post("/", response_model=Review)
def create_review(
    review: ReviewCreate,
    session: Session = Depends(get_session)
):

    data_dic = Review.model_validate(review)  # ReviewCreate object ko Review model mein convert karta hai
    print("✔ Review data validated and converted to Review model.")

    session.add(data_dic) # Session mein object add karta hai
    session.commit() # Changes database mein save karta hai
    session.refresh(data_dic) # Database se latest values object mein load karta hai
    print("✔ Review data saved to the database and refreshed.")
    
    return data_dic # Updated object response mein return karta hai

    # play_name: str = Field(index=True)
    # reviewer_name: str
    # rating: int = Field(ge=1, le=5)  # Rating between 1 and 5
    # comment: str