# Theater_app\src\utils\exception.py
from fastapi import Request
from fastapi.responses import JSONResponse


from typing import Any


class InvalidReviewError(Exception):
    def __init__(self, error_status_code: int = 404, param_play_name: str = "", reason: str = "Invalid Review"):
        self.error_status_code = error_status_code
        self.param_play_name = param_play_name
        self.reason = reason

# construtio function , variable , parameters
# self current object ko represent karta hai.

async def invalid_review_error_handler(request: Request, exc: Any):
    status_code = getattr(exc, "error_status_code", 400)
    reason = getattr(exc, "reason", "Invalid Review")
    play_name = getattr(exc, "param_play_name", "")
    return JSONResponse(
        status_code=status_code,
        content={
            "error": reason,
            "play_name": play_name
        }
    )



# Simple flow:
# Review nahi mila
#       ↓
# InvalidReviewError  ← custom class
#       ↓
# invalid_review_error_handler() ← custom function
#       ↓
# JSONResponse ← Library ka response
#       ↓
# Client ko error
