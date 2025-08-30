from typing import TYPE_CHECKING

from fastapi import HTTPException, status

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Product

from .schemas import ProductCreate, ProductUpdate

if TYPE_CHECKING:
    from core.models import User


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).order_by(Product.id)
    result: Result = await session.execute(stmt)

    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(
    session: AsyncSession, product_in: ProductCreate, user: "User"
) -> Product:
    product = Product(**product_in.model_dump(), user_id=user.id)
    session.add(product)
    await session.commit()

    return product


async def update_product(
    session: AsyncSession,
    product_id: int,
    product_in: ProductUpdate,
) -> Product:
    result = await session.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product does not exist",
        )

    update_data = product_in.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(product, key, value)

    await session.commit()
    await session.refresh(product)

    return product
