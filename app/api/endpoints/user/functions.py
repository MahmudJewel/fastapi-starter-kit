from fastapi import HTTPException, status, Depends
from typing import Annotated
from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

# from auth import models, schemas
from passlib.context import CryptContext
from jose import JWTError, jwt

# import 
from app.models import user as UserModel
from app.schemas.user import User, UserCreate


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# get user by email 
def get_user_by_email(db: Session, email: str):
    return db.query(UserModel.User).filter(UserModel.User.email == email).first()

# get user by id
def get_user_by_id(db: Session, user_id: int):
    db_user = db.query(UserModel.User).filter(UserModel.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# crete new user 
def create_new_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    new_user = UserModel.User(email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

