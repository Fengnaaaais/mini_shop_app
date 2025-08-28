from typing import TYPE_CHECKING
from .base import Base

from sqlalchemy.orm import Mapped, relationship

from core.mixins import IDColumnMixin


if TYPE_CHECKING:
    from .products import Proudct


class Category(Base, IDColumnMixin):
    title: Mapped[str]
    products: Mapped[list["Product"]] = relationship(back_populates="category")
    image: Mapped[str]
