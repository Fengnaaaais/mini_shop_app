from typing import TYPE_CHECKING
from .base import Base

from sqlalchemy.orm import Mapped, relationship


if TYPE_CHECKING:
    from .products import Proudct


class Category(Base):
    title: Mapped[str]
    products: Mapped[list["Product"]] = relationship(back_populates="category")
    image: Mapped[str]
