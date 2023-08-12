import random
from datetime import datetime

def generate_otp(): 
    return random.randint(100000, 999999)

def verify_otp(otp):
    current_time = datetime.now()

    if otp["EAT"] <= current_time or not otp["is_valid"]:
        return False
    
    return True