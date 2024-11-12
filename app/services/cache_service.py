import json
import uuid
import numpy as np
from app.config import config
from app.utils.similarity import get_similarity_score
from sentence_transformers import SentenceTransformer
import redis.asyncio as redis

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
r = redis.from_url(config.REDIS_URL)

async def process_prompt(prompt, threshhold, team_id):
    new_embedding = model.encode(prompt,convert_to_tensor=True)
    similarity_threshold = 0.8
    async for key in r.scan_iter("prompt:*"):
        cached_data = json.loads(await r.get(key))
        cached_prompt = cached_data['prompt']
        cached_embedding = np.array(cached_data['embedding'])

        similarity_score = get_similarity_score(new_embedding,cached_embedding)

        if similarity_score >= similarity_threshold:
          return {"cached":True, "response":cached_data['response'],"similarity":similarity_score}
    response = f"Generated response for prompt:{prompt}"
   
    cache_key = f"prompt:{uuid.uuid4()}"
    await r.set(cache_key,json.dumps({
       "prompt":prompt,
       "embedding":new_embedding.cpu().tolist(),
       "response":response
    }))
    return {"cached":False,"response":response}

async def save_to_cache(prompt, response, embedding=None):
    cache_key = f"prompt:{uuid.uuid4()}"
    await r.set(cache_key, json.dumps({
       "prompt": prompt,
       "response": response,
       "embedding": embedding or model.encode(prompt, convert_to_tensor=True).cpu().numpy().tolist()
    }))
    return {"status": "saved", "cache_key": cache_key}

async def list_cache():
    keys = []
    async for key in r.scan_iter("prompt:*"):
        cached_data = json.loads(await r.get(key))
        keys.append(cached_data)
    return keys