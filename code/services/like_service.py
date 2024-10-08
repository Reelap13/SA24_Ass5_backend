from repositories.like_repository import LikeRepository
from schemas.response_models import ResponseData

class LikeService:
    def __init__(self, user_repository: LikeRepository):
        self.like_repository = user_repository

    async def like_message(self, username: str, message_id: int) -> ResponseData:

        existing_like = await self.like_repository.get_like(username, message_id)
        if existing_like:
            await self.like_repository.remove_like(username, message_id)
            return ResponseData(
                code=200,
                message="Success deleting like",
                data=False
            )

        await self.like_repository.like_message(username, message_id)
        return ResponseData(
                code=200,
                message="Success creating like",
                data=True
            )

    async def get_likes_for_message(self, message_id: int) -> ResponseData:
        message_likes = await self.like_repository.get_likes_for_message(message_id)
        likes = []
        for message_like in message_likes:
            if message_like:
                likes.append(message_like.username)
        return ResponseData(
                code=200,
                message="Success getting likes for message",
                data=likes
            )
