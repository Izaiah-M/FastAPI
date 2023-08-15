import random
from datetime import datetime
from config.db_config import otp_collection


def generate_otp():
    return random.randint(100000, 999999)


async def verify_otp(otp):
    current_time = datetime.now()

    if otp["is_valid"] == False:
        return False
    elif otp["expiresAt"] <= current_time:
        try:
            print("Otp expired: updating db....")
            updated_result = await otp_collection.update_one(
                {"phone": otp["phone"], "otp": otp["otp"]},
                {"$set": {"is_valid": False}},
            )

            if updated_result.modified_count == 1:
                print("Otp expired: finished updating the db.")
                return False
            else:
                raise Exception("Something went wrong")
        except:
            return False
    else:
        return True
