from fastapi import FastAPI
from routes import user_routes, otp_routes

app = FastAPI()

# Registering our routes
app.include_router(user_routes.user_router)
app.include_router(otp_routes.otp)



# if __name__ == "__main__":
#     uvicorn.run(app, host='0.0.0.0', port=6000, debug=True)