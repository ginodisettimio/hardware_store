import bcrypt
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from server.database.models import BaseModel


class UserModel(BaseModel):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(String(length=50), unique=True, nullable=False)
    encrypted_password: Mapped[str] = mapped_column(String(length=100), nullable=False)
    email: Mapped[str] = mapped_column(String(length=200), unique=True, nullable=False)
    role: Mapped[str] = mapped_column(String(length=20), nullable=False)

    products = relationship('HardwareModel', back_populates='buyer')

    @property
    def password(self) -> str:
        return self.encrypted_password
    
    @password.setter
    def password(self, plain_password: str) -> None:
        hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())
        self.encrypted_password = hashed_password.decode('utf-8')

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
