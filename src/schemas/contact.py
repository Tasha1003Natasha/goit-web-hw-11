from typing import Optional
from datetime import date
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class ContactSchema(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    surname: str = Field(min_length=3, max_length=50)
    email: EmailStr
    phone: str = Field(max_length=20)
    birthday: date
    info: str | None = Field(default=None, max_length=250)


class ContactUpdateSchema(ContactSchema):
    completed: bool


class ContactResponse(BaseModel):
    id: int

    model_config = ConfigDict(from_attributes=True)
