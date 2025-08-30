from typing import TYPE_CHECKING

from sqlalchemy import (
    Integer,
    ForeignKey,
)
from sqlalchemy.orm import (
    mapped_column,
    Mapped,
)
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyBaseAccessTokenTable,
    SQLAlchemyAccessTokenDatabase,
)

from .base import Base
from core.types import user_id_type

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[user_id_type]):
    user_id: Mapped[user_id_type] = mapped_column(
        Integer,
        ForeignKey("user.id", ondelete="cascade"),
        nullable=False,
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyAccessTokenDatabase(session, cls)
