from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import Integer, ForeignKey

from .base import Base


if TYPE_CHECKING:
    from .category import Category


class Product(base):
    title: Mapped[str]
    description: Mapped[str]

    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("cateogry.id"))
    category: Mapped["Category"] = relationship(back_populates="products")

    price: Mapped[int]
    image: Mapped[str]
