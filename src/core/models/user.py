from typing import TYPE_CHECKING

from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.orm import Mapped, relationship

from core.types import user_id_type
from core.mixins import IDColumnMixin

from .base import Base


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from .product import Product


class User(Base, IDColumnMixin, SQLAlchemyBaseUserTable[user_id_type]):
    products: Mapped[list["Product"]] = relationship("Product", back_populates="user")

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
