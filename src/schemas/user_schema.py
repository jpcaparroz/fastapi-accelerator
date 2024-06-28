from datetime import datetime

from uuid import UUID

from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr


class BaseUserSchema(BaseModel):
    user_name: str
    user_email: EmailStr
    is_admin: bool = False


class CreateUserSchema(BaseUserSchema):
    user_password: str


class UpdateUserSchema(BaseUserSchema):
    user_name: Optional[str]
    user_password: Optional[str]
    user_email: Optional[EmailStr]
    is_admin: Optional[bool]


class GetUserSchema(BaseUserSchema):
    id: int
    user_uuid: Optional[UUID] = None
    created_on: Optional[datetime] = None
    updated_on: Optional[datetime] = None

