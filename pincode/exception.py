#  exception.py

from fastapi import Request
from fastapi.responses import JSONResponse


class InvalidPinCodeError(Exception):

    def __init__(
        self,
        error_status_code: int,
        pincode: str,
        reason: str = "Invalid format"
    ):
        self.error_status_code = error_status_code
        self.pincode = pincode
        self.reason = reason


async def invalid_pincode_error_hnadler(
    request: Request,
    exc: InvalidPinCodeError
):
    return JSONResponse(
        status_code=exc.error_status_code,
        content={
            "error": "Invalid Pincode",
            "message": f"pincode '{exc.pincode}' is invalid: {exc.reason}",
            "pincode": exc.pincode
        }
    )