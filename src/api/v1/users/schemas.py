from fastapi_users import schemas

from core.types import user_id_type


class UserSchema(schemas.BaseUser[user_id_type]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
