from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy.ext.asyncio.session import AsyncSession

from config.settings import settings


class DBDependency:
    def __init__(self):
        self._engine = self.get_engine
        self._session_factory = self.async_session_factory

    @property
    def get_engine(self):
        return create_async_engine(
            settings.db_settings.build_db_url,
            echo=settings.db_settings.db_echo,
        )

    @property
    def async_session_factory(self):
        return async_sessionmaker(
            bind=self._engine,
            expire_on_commit=False,
            autocommit=False,
        )

    @property
    def db_session(self) -> async_sessionmaker[AsyncSession]:
        return self._session_factory
