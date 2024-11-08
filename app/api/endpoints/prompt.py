from fastapi import APIRouter,Body
import json
import uuid
import numpy as np
from sentence_transformers import SentenceTransformer 
import redis.asyncio as redis
router = APIRouter()

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
# r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
r = redis.from_url("redis://localhost:6379")

@router.post("/process_prompt/")

async def process_prompt(prompt: str = Body(...)):
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
    r.set(cache_key,json.dumps({
       "prompt":prompt,
       "embedding":new_embedding.cpu().tolist(),
       "response":response
    }))
    return {"cached":False,"response":response}


def get_similarity_score(embedding1, embedding2):
    embedding1 = embedding1.cpu().numpy() if hasattr(embedding1, 'cpu') else embedding1
    embedding2 = embedding2.cpu().numpy() if hasattr(embedding2, 'cpu') else embedding2
    return np.dot(embedding1, embedding2) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))