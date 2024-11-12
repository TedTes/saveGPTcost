import os

class Config:
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY", "default-api-key")
    RATE_LIMIT = int(os.getenv("RATE_LIMIT", 10)) 

config = Config()
