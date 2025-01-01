from sqlalchemy import Column, String, Enum
from enum import Enum as PythonEnum

from app.core.database import Base
from .common import CommonModel
from app.utils.constant.globals import UserRole

class User(CommonModel):
	__tablename__ = "users"

	email = Column(String, unique=True, index=True)
	password = Column(String)
	first_name = Column(String, nullable=True)
	last_name = Column(String, nullable=True)
	role = Column(Enum(UserRole), default=UserRole.USER)

	def __repr__(self):
		return f"{self.email}"
	
metadata = Base.metadata

