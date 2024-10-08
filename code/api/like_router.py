from fastapi import APIRouter, HTTPException
from services.like_service import LikeService
from repositories.like_repository import LikeRepository
from services.response_service import handle_request
from schemas.response_models import ResponseData

router = APIRouter()

like_service = LikeService(LikeRepository())

@router.patch("/like")
async def like_message(data: dict) -> ResponseData:
    username = data.get("username")
    message_id = data.get("messageId")

    if not username or not message_id:
        raise HTTPException(status_code=400, detail="Username and messageId are required")

    return await handle_request(lambda: like_service.like_message(username, message_id))

@router.get("/likes")
async def get_likes(message_id: int) -> ResponseData:
    return await handle_request(lambda: like_service.get_likes_for_message(message_id))
