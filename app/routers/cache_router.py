from fastapi import APIRouter,Body
import json
import uuid
import numpy as np
from sentence_transformers import SentenceTransformer 
from utils.similarity import get_similarity_score
import redis.asyncio as redis
from app.services.cache_service import process_prompt,list_cache,save_to_cache
cache_router = APIRouter()

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
# r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
r = redis.from_url("redis://localhost:6379")

@cache_router.post("/process_prompt/")
async def process_prompt_endpoint(prompt: str = Body(...),threshold:float = 0.8, team_id:str = None):
    response = await process_prompt(prompt,threshold, team_id)
    return response
@cache_router.post("/save")
async def save_to_cache_endpoint(prompt: str = Body(...), response: str = Body(...), embedding: list = None):
    result = await save_to_cache(prompt, response, embedding)
    return result
@cache_router.get("/list")
async def list_cache_endpoint():
    return await list_cache()
@cache_router.delete("/{cache_key}")

@cache_router.get("/analytics/")
@cache_router.patch("/expire/{cache_key}")
@cache_router.delete("/clear")
@cache_router.post("/register-team")
@cache_router.post("/update-team-key/{team_id}")
async def test():
   print("hello")