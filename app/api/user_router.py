from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import AsyncSessionLocal
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.schemas.user import UserCreate, UserRead

router = APIRouter()


async def get_session():
    """
    Получении сессии БД
    """
    async with AsyncSessionLocal() as session:
        yield session


async def get_user_service(
    session: AsyncSession = Depends(get_session)
):
    """
    Dependency для создания сервиса.
    """
    repo = UserRepository(session)
    return UserService(repo)


@router.post("/", response_model=UserRead)
async def create_user(
    data: UserCreate,
    service: UserService = Depends(get_user_service)
):
    """
    Эндпоинт создания пользователя.
    """
    return await service.create_user(data)


@router.get("/", response_model=list[UserRead])
async def list_users(
    service: UserService = Depends(get_user_service)
):
    """
    Эндпоинт получения списка пользователей.
    """
    return await service.list_users()