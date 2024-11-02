from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float

from server.database.models import BaseModel


class HardwareModel(BaseModel):
    __tablename__ = 'products'

    name: Mapped[str] = mapped_column(String(length=50), nullable=False)
    kind: Mapped[str] = mapped_column(String(length=50), nullable=False)
    brand: Mapped[str] = mapped_column(String(length=50), nullable=False)
    distributor: Mapped[str] = mapped_column(String(length=50), nullable=False)
    price: Mapped[float] = mapped_column(Float(precision=3), nullable=False)
