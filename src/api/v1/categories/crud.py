from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Category
from .schemas import CategoryCreate


async def get_categories(session: AsyncSession):
    stmt = select(Category).order_by(Category.id)
    result: Result = await session.execute(stmt)

    categories = result.scalars().all()
    return list(categories)


async def get_category(session: AsyncSession, category_id: int) -> Category | None:
    return await session.get(Category, category_id)


async def create_category(
    session: AsyncSession, category_in: CategoryCreate
) -> Category:
    category = Category(**category_in.model_dump())
    session.add(category)
    await session.commit()

    return category


async def update_category(
    session: AsyncSession,
    category_id: int,
    category_in,
) -> Category:
    stmt = select(Category).where(Category.id == category_id)
    result: Result = await session.execute(stmt)
    category = result.scalar_one_or_none()

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category does not exict"
        )

    for key, value in category_in.dict(exclude_unset=True).items():
        setattr(category, key, value)

    await session.commit()
    await session.refresh(category)

    return category
