from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.user import UserRole

class UserBase(BaseModel):
	email: str

class UserCreate(UserBase):
	first_name: Optional[str]
	last_name: Optional[str]
	password: str

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
	first_name: Optional[str]
	last_name: Optional[str]
	is_active: bool
	role: UserRole or None

class Token(BaseModel):
    access_token: str
    token_type: str



