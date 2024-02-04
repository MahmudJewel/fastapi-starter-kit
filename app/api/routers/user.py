from fastapi import APIRouter
from app.api.endpoints.user.user import user_module


user_router = APIRouter()

user_router.include_router(
    user_module,
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)




