from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def home():
    return {"mensagem": "API FreelancerBot funcionando!"}
