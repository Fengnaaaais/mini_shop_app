from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from .crud import get_categories, get_category, create_category, update_category
from .schemas import CategorySchema, CategoryCreate, CategoryUpdate


router = APIRouter()


@router.get("/")
async def get_categories_view(
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
) -> list[CategorySchema]:
    return await get_categories(session=session)


@router.get("/{category_id}")
async def get_category_view(
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
    category_id: int,
) -> CategorySchema | None:
    return await get_category(
        session=session,
        category_id=category_id,
    )


@router.post("/create")
async def create_category_view(
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
    category_in: CategoryCreate,
) -> CategorySchema:
    return await create_category(session=session, category_in=category_in)


@router.patch("/{category_id}")
async def update_category_view(
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
    category_id: int,
    category_in: CategoryUpdate,
) -> CategorySchema:
    return await update_category(
        session=session,
        category_id=category_id,
        category_in=category_in,
    )
