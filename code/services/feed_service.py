from repositories.message_repository import MessageRepository
from repositories.user_message_repository import UserMessageRepository
from services.like_service import LikeService
from schemas.response_models import ResponseData

class FeedService:

    def __init__(self, message_repository: MessageRepository, user_message_repository: UserMessageRepository, like_service: LikeService):
        self.message_repository = message_repository
        self.user_message_repository = user_message_repository
        self.like_service = like_service

    async def get_last_messages(self, limit: int = 10) -> ResponseData:
        messages = await self.message_repository.get_last_messages(limit)
        print(len(messages), limit)
        feed = []
        for message in messages:
            if message:
                feed.append({ 
                    "messageId": message.id,
                    "text": message.text,
                    "username": (await self.user_message_repository.get_username_by_message_id(message.id)).username,
                    "liked": (await self.like_service.get_likes_for_message(message.id)).data
                })

        return ResponseData(
                code=200,
                message="Success getting last",
                data=feed
            )
