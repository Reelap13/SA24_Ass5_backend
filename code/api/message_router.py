from fastapi import APIRouter, HTTPException
from services.message_service import MessageService
from services.response_service import handle_request
from repositories.message_repository import MessageRepository
from repositories.user_message_repository import UserMessageRepository
from services.like_service import LikeService 
from repositories.like_repository import LikeRepository
from schemas.response_models import ResponseData

router = APIRouter()

message_service = MessageService(MessageRepository(), UserMessageRepository(), LikeService(LikeRepository()))

@router.post("/new")
async def create_message(data: dict) -> ResponseData:
    username = data.get("username")
    text = data.get("text")

    if not username or not text:
        raise HTTPException(status_code=400, detail="Username and text are required")

    return await handle_request(lambda: message_service.create_message_for_user(username, text))


@router.get("/wall")
async def get_user_messages(username: str) -> ResponseData:
    if not username:
        raise HTTPException(status_code=400, detail="Username is required")

    return await handle_request(lambda: message_service.get_user_messages(username))