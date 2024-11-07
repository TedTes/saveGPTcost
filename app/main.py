from fastapi import FastAPI
from app.api.endpoints import prompt

app = FastAPI()

app.include_router(prompt.router)
