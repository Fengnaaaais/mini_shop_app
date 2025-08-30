from typing import Annotated
from annotated_types import MaxLen, MinLen

from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    title: Annotated[str, MaxLen(100), MinLen(10)]
    description: str
    category_id: int
    price: int
    image: str


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    title: Annotated[str, MaxLen(100), MinLen(10)] | None = None
    description: str | None = None
    category_id: int | None = None
    price: int | None = None
    image: str | None = None


class ProductSchema(ProductBase):
    id: int
    user_id: int

    model_config = ConfigDict(
        from_attributes=True,
    )
