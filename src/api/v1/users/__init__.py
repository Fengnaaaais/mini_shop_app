from fastapi import APIRouter

from ..dependencies.authentication.fastapi_users import fastapi_users
from ..dependencies.authentication.authentication_backend import auth_backend

from .schemas import UserSchema, UserCreate, UserUpdate


router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserSchema, UserCreate),
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_users_router(UserSchema, UserUpdate),
    prefix="/users",
    tags=["Users"],
)
