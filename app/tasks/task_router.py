from dependency_injector.wiring import inject, Provide
from fastapi import Depends, APIRouter

from .dto.create_task_dto import CreateTaskDto
from .dto.task_dto import TaskDto
from .task_service import TaskService
from ..container import Container
from ..shared.dto.result_dto import ResultDto

router = APIRouter()

ServiceDep = Depends(Provide[Container.task_service])


@router.get("/tasks")
@inject
async def get_tasks(service: TaskService = ServiceDep) -> ResultDto[list[TaskDto]]:
    return ResultDto(
        result=[TaskDto.from_entity(task_entity) for task_entity in service.get_tasks()]
    )


@router.post("/task", status_code=201)
@inject
async def create_task(text: CreateTaskDto, service: TaskService = ServiceDep) -> ResultDto[TaskDto]:
    return ResultDto(result=TaskDto.from_entity(service.create_task(text.text)))


@router.put("/task")
@inject
async def update_task(task_dto: TaskDto, service: TaskService = ServiceDep) -> ResultDto[TaskDto]:
    return ResultDto(result=TaskDto.from_entity(service.update_task(task_dto.to_entity())))


@router.delete("/task/{task_id}")
@inject
async def delete_task(task_id: int, service: TaskService = ServiceDep):
    service.delete_task(task_id)
