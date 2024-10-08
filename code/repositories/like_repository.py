from models import likes
from database import database

class LikeRepository:
    
    async def like_message(self, username: str, message_id: int):
        query = likes.insert().values(username=username, message_id=message_id)
        await database.execute(query)

    async def get_likes_for_message(self, message_id: int):
        query = likes.select().where(likes.c.message_id == message_id)
        return await database.fetch_all(query)

    async def get_like(self, username: str, message_id: int):
        query = likes.select().where(
            likes.c.username == username,
            likes.c.message_id == message_id
        )
        return await database.fetch_one(query)

    async def remove_like(self, username: str, message_id: int):
        query = likes.delete().where(
            likes.c.username == username,
            likes.c.message_id == message_id
        )
        await database.execute(query)