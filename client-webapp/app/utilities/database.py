from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.settings import Settings


def _get_db_url(app_settings: Settings) -> str:
    return f"postgresql+asyncpg://{app_settings.DB_USER}:{app_settings.DB_PASSWORD}@{app_settings.DB_HOST}:{app_settings.DB_PORT}/{app_settings.DB_NAME}?options=-csearch_path={app_settings.DB_SCHEMA}"


def create_session_factory(app_settings: Settings) -> async_sessionmaker[AsyncSession]:
    url = _get_db_url(app_settings)
    engine = create_async_engine(
        url,
        echo=True,
        pool_size=20,
        max_overflow=20,
        echo_pool=False,
        hide_parameters=False,
        pool_pre_ping=True,
        pool_recycle=360,
    )
    return async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
