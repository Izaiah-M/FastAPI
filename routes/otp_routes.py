from fastapi import APIRouter
from models.otp import OTPRequest, OTPVerification
from helpers.status_codes import STATUS_CODE_MISSING_FIELDS_400
from config.db_config import otp_collection
from helpers.otp import generate_otp

otp = APIRouter(prefix="/api/otp", tags=["OTP"])

@otp.post("/") 
async def create_otp(req: OTPRequest):
    if not req.phoneNumber:
        return STATUS_CODE_MISSING_FIELDS_400
    
    otp = generate_otp()
    
    return {"OTP" : otp}
    
@otp.post("/validate") 
async def validate_otp(req: OTPVerification):
    if not req.phoneNumber or not req.otp:
        return STATUS_CODE_MISSING_FIELDS_400
    
