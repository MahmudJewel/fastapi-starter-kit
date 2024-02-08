# fastapi
from fastapi import FastAPI
from app.core.modules import init_routers, make_middleware


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="FastAPI starter kit",
        description="FastAPI starter kit that is needed for every fastapi project. The repo is developed with 💗 by mahmud.",
        version="1.0.0",
        # dependencies=[Depends(Logging)],
        middleware=make_middleware(),
    )
    init_routers(app_=app_)
    return app_


app = create_app()
