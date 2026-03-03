from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User


class UserRepository:
    """
    Работа с БД без бизнес логики
    """

    def __init__(self, session: AsyncSession):
        self.session = session


    async def create(self, email: str, name: str) -> User:
        user = User(email=email, name=name)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user


    async def get_all(self):
        result = await self.session.execute(select(User))
        return result.scalars().all()
