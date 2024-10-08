from fastapi import APIRouter, HTTPException
from services.response_service import handle_request
from services.user_service import UserService
from repositories.user_repository import UserRepository
from schemas.response_models import ResponseData

router = APIRouter()

user_service = UserService(UserRepository())

@router.post("/login")
async def login_user(data: dict) -> ResponseData:
    username = data.get("username")
    
    if not username:
        raise HTTPException(status_code=400, detail="Username is required")

    return await handle_request(lambda: user_service.register_user(username))
