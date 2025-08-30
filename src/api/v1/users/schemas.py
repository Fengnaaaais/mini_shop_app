from typing import TYPE_CHECKING

from fastapi_users import schemas

from core.types import user_id_type

from ..products.schemas import ProductSchema


class UserSchema(schemas.BaseUser[user_id_type]):
    products: list["ProductSchema"] = []


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


UserSchema.model_rebuild()
