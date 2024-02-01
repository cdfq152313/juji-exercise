from fastapi import FastAPI

from .container import Container
from .tasks import task_router


def create_app() -> FastAPI:
    container = Container()

    app = FastAPI()
    app.container = container
    app.include_router(task_router.router)
    return app


app = create_app()
