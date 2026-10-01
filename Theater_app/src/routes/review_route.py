# Theater_app\src\routes\review_route.py
from dataclasses import field
from dataclasses import field
from typing import List
from fastapi import APIRouter, Depends
from validator.review_create_interface import ReviewCreate, ReviewUpdate
from src.utils.api_response import AvgResponse, ReviewResponse, ReviewAvgResponse
from src.utils.exception import InvalidReviewError
from sqlmodel import Session, select, func
from src.db.engine import get_session
from src.model.model import Review


import rich

router = APIRouter(prefix="/review", tags=["review"])

# POST localhost:8000/review
@router.post("/", response_model=Review)
def create_review(
    review: ReviewCreate,
    session: Session = Depends(get_session)
):

    data_dic = Review.model_validate(review)  # ReviewCreate object convert into Review model.
    print("✔ Review data validated and converted to Review model.")

    session.add(data_dic) # Add Object in session to track it for database operations
    session.commit() # changes save in to database permanently
    session.refresh(data_dic) # Refresh the object with the latest values from the database
    print("✔ Review data saved to the database and refreshed.")
    
    return data_dic # Return the created review object

    # play_name: str = Field(index=True)
    # reviewer_name: str
    # rating: int = Field(ge=1, le=5)  # Rating between 1 and 5
    # comment: str
    

# GET localhost:8000/reviews
@router.get("/", response_model=ReviewResponse)
def list_reviews(play_name: str | None = None,offset: int =0, limit:int=5, session: Session = Depends(get_session)):

    statement = select(Review)

    if play_name:
        statement = statement.where(Review.play_name == play_name)
    
    query = statement.offset(offset).limit(limit)
    result = session.exec(query) # to execute select query into database
    reviews = result.all() # to extract all entries of Review table

    if not reviews:
        raise InvalidReviewError(404, play_name or "", f"No data found for {play_name}")

    return ReviewResponse(count=len(reviews), items=list(reviews))

# GET localhost:8000/reviews/average/(play_name)
@router.get("/average/{play_name}")
def get_average_rating(play_name: str, session: Session = Depends(get_session)):
     
    statement = select(func.avg(Review.rating),func.count(Review.id)).where(Review.play_name == play_name)
    result = session.exec(statement).first() # to execute select query into database

    avg_rating, total_reviews = result
    if(total_reviews == 0):
        raise InvalidReviewError(404, play_name or "", f"No reviews found for {play_name}")


    return ReviewAvgResponse(count=total_reviews, items=AvgResponse(play_name=play_name, average_rating=avg_rating, total_reviews=total_reviews))

# =------------------------------------------------------------
@router.patch("/{id}", response_model=Review)
def update_review(
    id: int,
    review: ReviewUpdate,
    session: Session = Depends(get_session)  

):
    existing_review = session.get(Review, id)

    if not existing_review:
        raise InvalidReviewError(
            404,
            str(id),
            f"Review with id {id} not found"
        )

    if review.play_name is not None:
        existing_review.play_name = review.play_name
    if review.reviewer_name is not None:
        existing_review.reviewer_name = review.reviewer_name
    if review.rating is not None:
        existing_review.rating = review.rating
    if review.comment is not None:
        existing_review.comment = review.comment

    session.add(existing_review) 
    session.commit() 
    session.refresh(existing_review)

    return existing_review

#-------------------------------------------------------------

@router.put("/{id}")
def update_review(id: int, review: ReviewCreate, session: Session = Depends(get_session)):
    existing_review = session.get(Review, id) # Search review by id in the database and return the existing review object if found.

    if not existing_review:
        raise InvalidReviewError(
            404, "", str(id), f"Review with id {id} not found"
        )

    for key, value in review.dict(exclude_unset=True).items():
        setattr(existing_review, key, value) 
    
    session.commit()  
    session.refresh(existing_review)

    return {"message": "Review updated successfully", "review": existing_review}

# -------------------------------------------------------------

@router.delete("/{id}")
def delete_review(
    id: int,
    session: Session = Depends(get_session)  # Database session FastAPI Depends(), through automatically provide .
):
    existing_review = session.get(Review, id) 
    # Searches the database for the review with the given id.
    # If the review is found, it will be stored in the existing_review variable.

    if not existing_review:
        raise InvalidReviewError(
            404,
            str(id),
            f"Review with id {id} not found"
        )

    session.delete(existing_review)
    session.commit()

    return {"message": "Review deleted successfully"}
