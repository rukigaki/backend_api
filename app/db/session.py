from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from core.config import settings


engine = create_async_engine(url=settings.db_url)

a_session_maker = async_sessionmaker(bind=engine)

async def get_db():
    async with a_session_maker() as session:
        yield session