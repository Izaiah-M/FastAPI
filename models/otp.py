from pydantic import BaseModel, Field


class OTPRequest(BaseModel):
    phoneNumber: str = Field(...)
    

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        
        json_schema_extra = {
            "example": {
               "phoneNumber": "0722306453"
            } 
        }

class OTPVerification(OTPRequest):
    otp: str = Field(...)
    
    
    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        
        json_schema_extra = {
            "example": {
               "phoneNumber": "0722306453",
               "otp":"189443"
            } 
        }
