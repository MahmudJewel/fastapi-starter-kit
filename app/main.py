# fastapi
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# sqlalchemy
from sqladmin import Admin, ModelView

from app.api.routers.api import router
from app.core.database import engine
from app.models.admin import UserAdmin


app = FastAPI()

origins = [
	# "http://localhost.tiangolo.com",
	# "https://localhost.tiangolo.com",
	# "http://localhost",
	# "http://localhost:8080",
    "*"
]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.get("/")
async def read_home_page():
    return {"msg": "Initialization done"}


app.include_router(router)

# ===========admin ===============
admin = Admin(app, engine)
admin.add_view(UserAdmin)
