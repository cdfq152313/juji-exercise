from typing import Callable

from fastapi import HTTPException, Request, Response
from fastapi.routing import APIRoute

from app.tasks.infra.repositories.in_memory_task_repository import NotFound


class TaskErrorRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            try:
                return await original_route_handler(request)
            except NotFound:
                await request.body()
                raise HTTPException(status_code=404, detail="Id not found")

        return custom_route_handler
