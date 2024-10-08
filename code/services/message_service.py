from repositories.message_repository import MessageRepository
from repositories.user_message_repository import UserMessageRepository
from services.like_service import LikeService
from schemas.response_models import ResponseData

class MessageService:
    def __init__(self, message_repository: MessageRepository, user_message_repository: UserMessageRepository, like_service: LikeService):
        self.message_repository = message_repository
        self.user_message_repository = user_message_repository
        self.like_service = like_service

    async def create_message_for_user(self, username: str, text: str) -> ResponseData:
        message_id = await self.message_repository.create_message(text)
        await self.user_message_repository.link_user_message(username, message_id)

        return ResponseData(
                code=201,
                message="Success creating user message",
                data=message_id
            )

    async def get_user_messages(self, username: str) -> ResponseData:
        user_messages = await self.user_message_repository.get_user_messages(username)
        messages = []
        for user_message in user_messages:
            message = await self.message_repository.get_message_by_id(user_message.message_id)
            if message:
                messages.append({ 
                    "messageId": message.id,
                    "text": message.text,
                    "username": username,
                    "liked": (await self.like_service.get_likes_for_message(message.id)).data
                })
        return ResponseData(
                code=200,
                message="Success getting user messages",
                data=messages
            )