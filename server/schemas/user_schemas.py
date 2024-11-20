from datetime import datetime

from pydantic import BaseModel, EmailStr

from server.enums import RoleEnum


class NewUserRequest(BaseModel):
    username: str
    password: str
    email: EmailStr
    role: str = RoleEnum.COMMON


class UpdateUserRequest(BaseModel):
    username: str | None = None
    password: str | None = None
    email: str | None = None
    role: str | None = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: RoleEnum
    created: datetime = datetime.now()
    updated: datetime = datetime.now()
