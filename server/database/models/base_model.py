from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from server.database import database_connection


class BaseModel(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement='auto')
    created: Mapped[datetime] = mapped_column(
        default=datetime.now, nullable=False)
    updated: Mapped[datetime] = mapped_column(
        default=datetime.now, onupdate=datetime.now, nullable=False)

    def to_dict(self) -> dict:
        return {
            column.name: getattr(self, column.name)
            for column in self.__class__.__table__.columns
        }
