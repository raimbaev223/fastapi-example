Example FastAPI

Небольшой пример backend-приложения на FastAPI.

Проект демонстрирует:

Разделение слоёв (Router => Service => Repository)

Асинхронную работу с БД

Валидацию данных

Dependency Injection

Автоматическую генерацию OpenAPI/Swagger

SQLite используется для демонстрации.

Стек технологий

Python 3.11+

FastAPI

SQLAlchemy (async)

SQLite

Структура проекта
app/

 ├── main.py
 
 ├── db/
 
 ├── models/
 
 ├── schemas/
 
 ├── repositories/
 
 ├── services/
 
 └── api/

Архитектура:

API (роутеры) — HTTP слой

Service — бизнес-логика

Repository — работа с БД

Models — ORM модели

Schemas — DTO для валидации

Установка и запуск

python -m venv venv

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

Установить зависимости:

pip install -r requirements.txt

Запуск сервера:

uvicorn app.main:app --reload

После запуска:

API: http://127.0.0.1:8000

Документация: http://127.0.0.1:8000/docs

Примечание:
Таблицы создаются автоматически при старте приложения.
