from datetime import datetime

from uuid import UUID

from typing import Optional

from pydantic import BaseModel
from pydantic import field_validator
from pydantic import EmailStr

from core.security import generate_hash


class BaseUserSchema(BaseModel):
    user_name: str
    user_email: EmailStr
    is_admin: bool = False


class CreateUserSchema(BaseUserSchema):
    user_password: str


    @field_validator("user_password", mode='before')
    def hash_password(cls, value) -> str:
        return generate_hash(value)


class UpdateUserSchema(BaseUserSchema):
    user_name: Optional[str]
    user_password: Optional[str]
    user_email: Optional[EmailStr]
    is_admin: Optional[bool]


class GetUserSchema(BaseUserSchema):
    id: int
    user_uuid: UUID
    created_on: datetime
    updated_on: Optional[datetime] = None

