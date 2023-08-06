from typing import Optional
from fastapi.responses import JSONResponse

def STATUS_CODE_200(data=None):
    return JSONResponse(content={"message": "Success", "data": data}, status_code=200)


STATUS_CODE_400 = JSONResponse(content={"message": "Bad Request"}, status_code=400)
STATUS_CODE_MISSING_FIELDS_400 = JSONResponse(content={"message": "Missing Fields!"}, status_code=400)
STATUS_CODE_404 = JSONResponse(content={"message": "Not Found"}, status_code=404)
STATUS_CODE_500 = JSONResponse(content={"message": "Internal Server error. Please try again later"}, status_code=500)
