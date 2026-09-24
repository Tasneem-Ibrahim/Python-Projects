# main.py

from fastapi import FastAPI
from pincode.data import PINCODES
from pincode.interface import LocationResponse, ResponseObject
from fastapi.middleware.cors import CORSMiddleware
from pincode.exception import InvalidPinCodeError, invalid_pincode_error_hnadler

app = FastAPI(
    title="pincode-project",
    description="Auto fill city, state and district from Pakistan pincode during checkout",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Exception class register in fastapi
app.add_exception_handler(InvalidPinCodeError, invalid_pincode_error_hnadler)

# Hello Api
@app.get("/")
def hello():
    return {"message": "FastAPI is working!"}


@app.get("/pincode/{id}", response_model=LocationResponse)
def lookup_pincode(id: str):
    
    if len(id) != 5:
        raise InvalidPinCodeError(error_status_code= 400, pincode=id, reason="digits must be 5")
    
    if not id.isdigit():
        raise InvalidPinCodeError(error_status_code= 400, pincode=id, reason="invalid pincode format, it must be in numbers")



    # if id not in PINCODES:
    #     raise HTTPException(status_code=404, detail="Pincode not found")
    
    
    return LocationResponse(result=PINCODES[id])