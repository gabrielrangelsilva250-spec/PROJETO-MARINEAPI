from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with Session() as session:
        yield session
