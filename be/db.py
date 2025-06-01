from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from db_config import DATABASE_URL

# 비동기 SQLAlchemy 엔진
engine = create_async_engine(DATABASE_URL, echo=True)

# 비동기 세션 팩토리
async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)