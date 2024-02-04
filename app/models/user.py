from sqlalchemy import Column, String, Enum
from enum import Enum as PythonEnum
from app.core.database import Base
from .common import CommonModel

class UserRole(str, PythonEnum):
	customer = "customer"
	vendor = "vendor"
	admin = "admin"

class User(CommonModel):
	__tablename__ = "users"

	email = Column(String, unique=True, index=True)
	password = Column(String)
	role = Column(Enum(UserRole), default=UserRole.customer)

metadata = Base.metadata
