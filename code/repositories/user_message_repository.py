from models import user_messages
from database import database

class UserMessageRepository:
    async def link_user_message(self, username: str, message_id: int):
        query = user_messages.insert().values(username=username, message_id=message_id)
        await database.execute(query)

    async def get_user_messages(self, username: str):
        query = user_messages.select().where(user_messages.c.username == username)
        return await database.fetch_all(query)
    
    async def get_username_by_message_id(self, message_id: int):
        query = user_messages.select().where(user_messages.c.message_id == message_id)
        return await database.fetch_one(query)
