from fastapi import APIRouter

router = APIRouter()

@router.post("/process_prompt/")
async def process_prompt(prompt: str):
    return {"message": "Processing prompt..."}
