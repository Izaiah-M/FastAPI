from fastapi import APIRouter
from models.otp import OTPRequest, OTPVerification
from helpers.status_codes import STATUS_CODE_MISSING_FIELDS_400, STATUS_CODE_500, STATUS_CODE_404
from config.db_config import otp_collection
from helpers.otp import generate_otp, verify_otp
from datetime import datetime, timedelta
from repository import repository

otp = APIRouter(prefix="/api/otp", tags=["OTP"])

@otp.post("/") 
async def create_otp(req: OTPRequest):
    if not req.phoneNumber: # consider verifying the phone number as well
        return STATUS_CODE_MISSING_FIELDS_400
    
    otp = generate_otp()

    expires_at = datetime.now() + timedelta(minutes=1)

    otp_log = {
        "phone": req.phoneNumber,
        "code": str(otp),
        "is_valid": True,
        "EAT": expires_at
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
    
    otp_log = await repository.get_one(otp_collection, {"phone" : req.phoneNumber, "code" : req.otp})

    if not otp_log:
        return STATUS_CODE_404
    
    is_valid = verify_otp(otp_log)

    if not is_valid:
        try:
            updateResult = await otp_collection.update_one({"phone" : req.phoneNumber, "code" : req.otp},  {"$set": {"is_valid": False}})

            if updateResult.modified_count == 1:
                return {"message" : "OTP is invalid!"}
            else:
                return {"message" : "OTP is invalid"}
        except:
            return STATUS_CODE_500
    
    try:
        result = await otp_collection.update_one({"phone" : req.phoneNumber, "code" : req.otp},  {"$set": {"is_valid": False}})

        if result.modified_count == 1:
            return {"is_valid" : True}
        else:
            return {"is_valid" : False}
        
    except:
        return STATUS_CODE_500
    

    

    
