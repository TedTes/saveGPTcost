from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException

class AuthenticationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        api_key = request.headers.get("X-API-KEY")
        if api_key != "secure-api-key":
            raise HTTPException(status_code=401, detail="Unauthorized")
        return await call_next(request)
