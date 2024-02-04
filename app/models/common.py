from sqlalchemy import Column, Boolean, Integer, String , DateTime, func
import uuid
from app.core.database import Base


class CommonModel(Base):
    __abstract__ = True

    # id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    id = Column(Integer, primary_key=True, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

