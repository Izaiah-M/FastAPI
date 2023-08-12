from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter

limiter = FastAPILimiter()
rate_limit = RateLimiter(times=2, seconds=5)

def rate_limited():
    return limiter.init(), rate_limit()