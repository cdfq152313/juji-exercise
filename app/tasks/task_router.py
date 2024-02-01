from typing import Annotated

from fastapi import Depends, APIRouter

from .task_service import TaskService

router = APIRouter()

ServiceDep = Annotated[TaskService, Depends(TaskService)]


@router.get("/tasks")
async def get_tasks(service: ServiceDep):
    return service.get_tasks()
