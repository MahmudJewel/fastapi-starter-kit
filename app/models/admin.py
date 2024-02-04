from fastapi import APIRouter, FastAPI
from sqladmin import Admin, ModelView
from app.core.database import engine
from app.models.user import User


class UserAdmin(ModelView, model=User):
    column_list = [
        User.id, 
        User.email,
        User.password,
        User.is_active,
        User.role,
        User.created_at,
        User.updated_at
        ]



