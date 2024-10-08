from fastapi import APIRouter
from services.response_service import handle_request
from services.feed_service import FeedService
from repositories.message_repository import MessageRepository
from repositories.user_message_repository import UserMessageRepository
from services.like_service import LikeService 
from repositories.like_repository import LikeRepository
from schemas.response_models import ResponseData

router = APIRouter()

feed_service = FeedService(MessageRepository(), UserMessageRepository(), LikeService(LikeRepository()))

@router.get("/feed")
async def get_feed() -> ResponseData:
    return await handle_request(lambda: feed_service.get_last_messages(10))
