from repositories.user_repository import UserRepository
from schemas.response_models import ResponseData

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def register_user(self, username: str) -> ResponseData:

        existing_user = await self.user_repository.get_user_by_username(username)
        if existing_user:
            return ResponseData(
                code=200,
                message="User login",
                data=dict(existing_user)
            )

        await self.user_repository.create_user(username)
        
        new_user = await self.user_repository.get_user_by_username(username)
        
        return ResponseData(
            code=201,
            message="User registered",
            data=dict(new_user)
        )
