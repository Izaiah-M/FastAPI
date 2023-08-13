from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from models.otp import OTPRequest, OTPVerification
from helpers.status_codes import STATUS_CODE_MISSING_FIELDS_400, STATUS_CODE_500, STATUS_CODE_404
from config.db_config import otp_collection, users_collection
from helpers.otp import generate_otp, verify_otp
from datetime import datetime, timedelta
from repository import repository
from slowapi import Limiter
from slowapi.util import get_remote_address
# from fastapi_limiter.depends import RateLimiter

limiter = Limiter(key_func=get_remote_address)

otp = APIRouter(prefix="/api/otp", tags=["OTP"])

# Consider using redis or memcache with fastapi_limiter

# @otp.post("/", dependencies=[Depends(RateLimiter(times=2, seconds=5))]) 
@otp.post("/") 
@limiter.limit("2/minute")
async def create_otp(req: OTPRequest, request: Request):
    if not req.phoneNumber: 
        return STATUS_CODE_MISSING_FIELDS_400
    
    # consider verifying the phone number as well
    
    user_exists = await repository.get_one(users_collection, {"phone": req.phoneNumber})

    if user_exists:
            return JSONResponse(content={"message": "User already exists"}, status_code=400)
    
    otp = generate_otp()

    expires_at = datetime.now() + timedelta(minutes=1)

    otp_log = {
        "phone": req.phoneNumber,
        "otp": str(otp),
        "is_valid": True,
        "expiresAt": expires_at
    }

    try:
        await otp_collection.insert_one(otp_log)

        return {"OTP" : str(otp)} 
    except:
        return STATUS_CODE_500
    
    
    
@otp.post("/validate") 
async def validate_otp(req: OTPVerification):
    if not req.phoneNumber or not req.otp:
        return STATUS_CODE_MISSING_FIELDS_400
    
    otp_log = await repository.get_one(otp_collection, {"phone" : req.phoneNumber, "otp" : req.otp})

    if not otp_log:
        return STATUS_CODE_404
    
    is_valid = verify_otp(otp_log)

    # print(is_valid)

    if not is_valid:
        try:
            await otp_collection.update_one({"phone" : req.phoneNumber, "otp" : req.otp},  {"$set": {"is_valid": False}})

            return JSONResponse(content={"message": "Invalid OTP!"}, status_code=400)

        except:
            return STATUS_CODE_500
    
    try:
        await otp_collection.update_one({"phone" : req.phoneNumber, "code" : req.otp},  {"$set": {"is_valid": False}})

        return {"is_valid" : "Y"}
       
    except:
        return STATUS_CODE_500
    

    

    
