from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from typing import AsyncGenerator
from db import async_session

# FastAPI 의존성으로 세션 관리
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session