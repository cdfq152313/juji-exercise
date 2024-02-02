from typing import Self

from pydantic import BaseModel

from app.tasks.entities.task_entity import TaskEntity


class TaskDto(BaseModel):
    id: int
    text: str
    status: int

    def to_entity(self):
        return TaskEntity(
            id=self.id,
            text=self.text,
            status=self.status == 1
        )

    @classmethod
    def from_entity(cls, entity: TaskEntity) -> Self:
        return TaskDto(
            id=entity.id,
            text=entity.text,
            status=1 if entity.status else 0
        )
