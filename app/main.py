from fastapi import FastAPI
from app.routers.cache_router import cache_router
from app.middleware.logging_middleware import LoggingMiddleware
from app.middleware.auth_middleware import AuthenticationMiddleware
from app.middleware.rate_limit_middleware import RateLimitingMiddleware
from app.middleware.timing_middleware import TimingMiddleware
from app.api.endpoints import prompt

app = FastAPI()

app.include_router(prompt.router,prefix="/api/v1/cache")
app.add_middleware(LoggingMiddleware)
app.add_middleware(AuthenticationMiddleware)
app.add_middleware(RateLimitingMiddleware)
app.add_middleware(TimingMiddleware)