from typing import Annotated
from annotated_types import MaxLen

from pydantic import BaseModel, ConfigDict


class CategoryBase(BaseModel):
    title: Annotated[str, MaxLen(50)]
    image: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):

    title: Annotated[str, MaxLen(50)] | None = None
    image: str | None = None


class CategorySchema(CategoryBase):
    id: int
    image: str

    model_config = ConfigDict(
        from_attributes=True,
    )
