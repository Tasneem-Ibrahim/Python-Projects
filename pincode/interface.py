#  interface.py

from pydantic import BaseModel

class ResponseObject(BaseModel):
    pincode: str
    city: str
    state: str
    district: str


class LocationResponse(BaseModel):
    status: str = "success"
    result: ResponseObject