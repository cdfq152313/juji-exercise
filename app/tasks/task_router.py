from dependency_injector.wiring import inject, Provide
from fastapi import Depends, APIRouter

from .dto.task_resp_dto import TaskRespDto
from .task_service import TaskService
from ..container import Container

router = APIRouter()

ServiceDep = Depends(Provide[Container.task_service])


@router.get("/tasks")
@inject
async def get_tasks(service: TaskService = ServiceDep):
    return {
        "result": [
            TaskRespDto.from_entity(task_entity) for task_entity in service.get_tasks()
        ]
    }
