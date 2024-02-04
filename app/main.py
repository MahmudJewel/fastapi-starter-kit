from fastapi import FastAPI

from app.api.routers.user import user_router

app = FastAPI()

@app.get('/')
async def read_home_page():
    return {"msg": "Initialization done"}


app.include_router(user_router)

