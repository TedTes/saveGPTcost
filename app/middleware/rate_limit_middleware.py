from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException
from time import time

rate_limit_cache = {}

class RateLimitingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        limit, interval = 10, 60  # 10 requests per minute
        current_time = time()
        request_times = rate_limit_cache.get(client_ip, [])
        request_times = [t for t in request_times if current_time - t < interval]

        if len(request_times) >= limit:
            raise HTTPException(status_code=429, detail="Rate limit exceeded")

        request_times.append(current_time)
        rate_limit_cache[client_ip] = request_times
        return await call_next(request)
