from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """
    Валидация входящих данных
    """
    email: EmailStr
    name: str


class UserRead(BaseModel):
    """
    DTO для ответа клиенту.
    """
    id: int
    email: EmailStr
    name: str

    class Config:
        from_attributes = True