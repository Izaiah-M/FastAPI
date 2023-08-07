from fastapi.responses import JSONResponse

def STATUS_CODE_201(data=None):
    return JSONResponse(content={"message": "Successfully Updated", "data": data}, status_code=201)


STATUS_CODE_400 = JSONResponse(content={"message": "Bad Request"}, status_code=400)
STATUS_CODE_MISSING_FIELDS_400 = JSONResponse(content={"message": "Missing Fields!"}, status_code=400)
STATUS_CODE_404 = JSONResponse(content={"message": "Not Found"}, status_code=404)
STATUS_CODE_500 = JSONResponse(content={"message": "Internal Server error. Please try again later"}, status_code=500)
