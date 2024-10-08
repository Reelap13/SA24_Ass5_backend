from models import users
from database import database

class UserRepository:
    async def create_user(self, username: str):
        query = users.insert().values(username=username)
        await database.execute(query)

    async def get_user_by_username(self, username: str):
        query = users.select().where(users.c.username == username)
        return await database.fetch_one(query)