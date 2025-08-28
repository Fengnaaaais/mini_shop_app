from typing import TYPE_CHECKING

from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from core.types import user_id_type
from core.mixins import IDColumnMixin

from .base import Base


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, IDColumnMixin, SQLAlchemyBaseUserTable[user_id_type]):
    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyBaseUserDatabase(session, cls)
