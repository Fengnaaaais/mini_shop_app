from typing import Annotated, TYPE_CHECKING

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper

from .crud import get_products, get_product, create_product, update_product
from .schemas import ProductSchema, ProductCreate, ProductUpdate
from ..dependencies.authentication.fastapi_users import fastapi_users

if TYPE_CHECKING:
    from core.models import User


router = APIRouter()


@router.get("/")
async def get_products_view(
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
) -> list[ProductSchema]:
    return await get_products(session=session)


@router.get("/{product_id}")
async def get_product_view(
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
    product_id: int,
) -> ProductSchema | None:
    return await get_product(
        session=session,
        product_id=product_id,
    )


current_user = fastapi_users.current_user()


@router.post("/create")
async def create_product_view(
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
    product_in: ProductCreate,
    user: Annotated["User", Depends(current_user)],
) -> ProductSchema:
    return await create_product(
        session=session,
        product_in=product_in,
        user=user,
    )


@router.patch("/{product_id}")
async def update_product_view(
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
    product_id: int,
    product_in: ProductUpdate,
) -> ProductSchema:
    return await update_product(
        session=session,
        product_id=product_id,
        product_in=product_in,
    )
