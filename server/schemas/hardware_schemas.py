from datetime import datetime

from pydantic import BaseModel


class NewHardwareRequest(BaseModel):
    name: str
    kind: str = ''
    brand: str = ''
    distributor: str = ''
    price: float = 0.0


class UpdateHardwareRequest(BaseModel):
    name: str | None = None
    kind: str | None = None
    brand: str | None = None
    distributor: str | None = None
    price: float | None = None


class HardwareResponse(BaseModel):
    id: int
    name: str
    kind: str | None = ''
    brand: str | None = ''
    distributor: str | None = ''
    price: float = 0.0
    created: datetime = datetime.now()
    updated: datetime = datetime.now()
