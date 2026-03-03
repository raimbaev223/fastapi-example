from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class UserService:
    """
    Сервисный слой с бизнес логикой.
    """

    def __init__(self, repo: UserRepository):
        self.repo = repo


    async def create_user(self, data: UserCreate):
        return await self.repo.create(data.email, data.name)


    async def list_users(self):
        return await self.repo.get_all()
