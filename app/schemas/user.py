from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.utils.constant.globals import UserRole

class UserBase(BaseModel):
	email: str

class UserCreate(UserBase):
	password: str
	first_name: str | None = None
	last_name: str | None = None

class UserLogin(UserBase):
	password: str

class User(UserBase):
	id: int
	first_name: Optional[str]
	last_name: Optional[str]
	is_active: bool
	role: UserRole or None
	created_at: datetime
	updated_at: datetime
	class Config:
		from_attributes = True

class UserUpdate(BaseModel):
	first_name: str | None = None
	last_name: str | None = None
	is_active: bool | None = None
	role: UserRole or None = None

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str



