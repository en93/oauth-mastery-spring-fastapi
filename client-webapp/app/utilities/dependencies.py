
from fastapi import Request
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession


async def get_session(request: Request):
    async_sessionmaker: async_sessionmaker[AsyncSession] = request.app.state.session_factory
    async with async_sessionmaker() as session:
        yield session
