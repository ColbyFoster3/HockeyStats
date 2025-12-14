from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import get_settings

settings = get_settings()
engine = create_engine(
    settings.database_url,
    echo=True,          # logs SQL (great while learning)
    future=True
)
engine2 = create_async_engine(settings.database_url, echo=True)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)
AsyncSessionLocal = async_sessionmaker(
    engine2,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass

# Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_db_async() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session