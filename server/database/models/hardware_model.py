from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Float, ForeignKey

from server.database.models import BaseModel


class HardwareModel(BaseModel):
    __tablename__ = 'products'

    name: Mapped[str] = mapped_column(String(length=50), nullable=False)
    kind: Mapped[str] = mapped_column(String(length=50), nullable=False)
    brand: Mapped[str] = mapped_column(String(length=50), nullable=False)
    distributor: Mapped[str] = mapped_column(String(length=50), nullable=False)
    price: Mapped[float] = mapped_column(Float(precision=3), nullable=False)
    IVA: Mapped[str] = mapped_column(String(4), default='21%' ,nullable=False)

    # Foreign_Key
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True)

    buyer = relationship('UserModel', back_populates='products')

    def to_dict(self):
        response = super().to_dict()
        if self.buyer:
            response['buyer'] = self.buyer.to_dict()
        return response
