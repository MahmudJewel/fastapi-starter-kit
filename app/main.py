from fastapi import FastAPI

from app.api.routers.user import user_router

from sqladmin import Admin, ModelView
from app.core.database import engine
from app.models.user import User

app = FastAPI()

@app.get('/')
async def read_home_page():
    return {"msg": "Initialization done"}


app.include_router(user_router)

admin = Admin(app, engine)
class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email]

admin.add_view(UserAdmin)

