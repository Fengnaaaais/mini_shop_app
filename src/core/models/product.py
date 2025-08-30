from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import Integer, ForeignKey

from core.mixins import IDColumnMixin
from core.types import user_id_type

from .base import Base


if TYPE_CHECKING:
    from .category import Category
    from .user import User


class Product(Base, IDColumnMixin):
    title: Mapped[str]
    description: Mapped[str]

    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("category.id"))
    category: Mapped["Category"] = relationship(back_populates="products")

    price: Mapped[int]
    image: Mapped[str]

    user_id: Mapped[user_id_type] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="products")
