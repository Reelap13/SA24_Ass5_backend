from models import messages
from database import database

class MessageRepository:
    async def create_message(self, text: str):
        query = messages.insert().values(text=text)
        return await database.execute(query)

    async def get_message_by_id(self, message_id: int):
        query = messages.select().where(messages.c.id == message_id)
        return await database.fetch_one(query)
    
    async def get_last_messages(self, limit: int):
        query = messages.select().order_by(messages.c.id.desc()).limit(limit)
        return await database.fetch_all(query)
