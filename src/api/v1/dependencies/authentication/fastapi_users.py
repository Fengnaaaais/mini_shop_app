from fastapi_users import FastAPIUsers

from core.models import User
from core.types import user_id_type

from .user_manager import get_user_manager
from .authentication_backend import auth_backend

fastapi_users = FastAPIUsers[User, user_id_type](
    get_user_manager,
    [auth_backend],
)
