from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from core.config import settings


class DataBaseHelper:
    def __init__(
        self,
        url: str | None = settings.db.url,
        echo: bool | None = settings.db.echo,
    ):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
        )

    async def session_dependency(self):
        async with self.session_factory() as session:
            yield session

            await session.close()


db_helper: DataBaseHelper = DataBaseHelper()
