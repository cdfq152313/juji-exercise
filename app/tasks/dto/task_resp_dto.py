from typing import Self

from pydantic import BaseModel

from app.tasks.entities.task_entity import TaskEntity


class TaskRespDto(BaseModel):
    id: int
    text: str
    status: int

    @classmethod
    def from_entity(cls, entity: TaskEntity) -> Self:
        return TaskRespDto(
            id=entity.id,
            text=entity.text,
            status=1 if entity.status else 0
        )
