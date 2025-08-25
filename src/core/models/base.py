from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column

from core.utils.case import to_snake


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr.directive
    def __tablename__(cls):
        return to_snake(cls.__name__)
