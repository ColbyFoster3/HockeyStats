from fastapi import APIRouter

router = APIRouter(prefix="/v1/users", tags=["users"])

@router.get("/")
async def get_users():
    return[{"username": "test"}]