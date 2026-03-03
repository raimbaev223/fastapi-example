from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.user_router import router as user_router
from app.db.session import engine, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Создаем таблицы БД один раз при старте.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield



app = FastAPI(
    title="Example FastAPI Backend",
    version="1.0.0",
    description="Пример backend-приложения с разделением слоёв",
    lifespan=lifespan,
)


# Подключаем роутеры
app.include_router(
    user_router,
    prefix="/users",
    tags=["Users"]
)


@app.get("/", tags=["Health"])
async def health_check():
    """
    Простой health-check эндпоинт.
    """
    return {"status": "ok"}