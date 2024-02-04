# fastapi 
from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated

# sqlalchemy
from sqlalchemy.orm import Session

# import
from app.core.dependencies import get_db, oauth2_scheme 
from app.schemas.user import User, UserCreate
from app.api.endpoints.user import functions as user_functions

user_module = APIRouter()


@user_module.get('/')
async def read_auth_page():
    return {"msg": "Auth page Initialization done"}

# create new user 
@user_module.post('/users', response_model=User)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_functions.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = user_functions.create_new_user(db, user)
    return new_user

