# fastapi
from fastapi import FastAPI

# sqlalchemy
from sqladmin import Admin, ModelView

from app.api.routers.user import user_router
from app.core.database import engine
from app.models.admin import UserAdmin


app = FastAPI()


@app.get("/")
async def read_home_page():
    return {"msg": "Initialization done"}


app.include_router(user_router)

# ===========admin ===============
admin = Admin(app, engine)
admin.add_view(UserAdmin)
