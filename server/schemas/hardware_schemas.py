from datetime import datetime

from pydantic import BaseModel

from server.schemas.user_schemas import UserResponse


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
    user_id: int

class HardwareResponse(BaseModel):
    id: int
    name: str
    kind: str
    brand: str
    distributor: str
    price: float = 0.0
    IVA: str = '21%'
    created: datetime = datetime.now()
    updated: datetime = datetime.now()

class BuyedHardwareResponse(BaseModel):
    id: int
    name: str
    kind: str
    brand: str
    distributor: str
    price: float = 0.0
    IVA: str = '21%'
    user_id: int
    buyer: UserResponse
    created: datetime = datetime.now()
    updated: datetime = datetime.now()
