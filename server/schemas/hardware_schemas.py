from datetime import datetime

from pydantic import BaseModel


class NewHardwareRequest(BaseModel):
    name: str
    kind: str = ''
    brand: str = ''
    distributor: str = ''
    price: float = ''


class UpdateHardwareRequest(BaseModel):
    name: str | None = None
    kind: str | None = None
    brand: str | None = None
    distributor: str | None = None
    price: float | None = None


class HardwareResponse(BaseModel):
    id: int
    name: str
    kind: str = ''
    brand: str = ''
    distributor: str = ''
    price: float = ''
    created: datetime
    updated: datetime
