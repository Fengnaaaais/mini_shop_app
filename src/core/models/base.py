from sqlalchemy.orm import DeclarativeBase, declared_attr

from core.utils.case import to_snake


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls):
        return to_snake(cls.__name__)
