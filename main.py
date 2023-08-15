from fastapi import FastAPI
from routes import user_routes, otp_routes
import redis.asyncio as redis

# from fastapi_limiter import FastAPILimiter
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded


limiter = Limiter(key_func=get_remote_address)

app = FastAPI()

# RateLimiting config
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# @app.on_event("startup")
# async def startup():
#     redis_init = redis.from_url("redis://localhost", encoding="utf-8", decode_responses=True)
#     await FastAPILimiter.init(redis_init)


# Registering our routes
app.include_router(user_routes.user_router)
app.include_router(otp_routes.otp)
