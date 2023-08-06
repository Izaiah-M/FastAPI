from fastapi import FastAPI
from routes.user_routes import user_router

app = FastAPI()

# Registering our routes
app.include_router(user_router)



# if __name__ == "__main__":
#     uvicorn.run(app, host='0.0.0.0', port=6000, debug=True)