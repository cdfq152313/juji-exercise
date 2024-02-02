from app.tasks.entities.task_entity import TaskEntity
from app.tasks.repositories.task_repository import TaskRepository


class InMemoryTaskRepository(TaskRepository):
    def __init__(self):
        self._counter = 0
        self._dict: [int, TaskEntity] = {}

    def get_all(self) -> list[TaskEntity]:
        return sorted(self._dict.values(), key=lambda task_entity: task_entity.id)

    def add(self, text: str) -> TaskEntity:
        obj = TaskEntity(id=self._counter, text=text, status=False)
        self._counter += 1
        self._dict[obj.id] = obj
        return obj

    def update(self, obj: TaskEntity):
        if obj.id not in self._dict:
            raise NotFound()
        self._dict[obj.id] = obj
        return obj

    def delete(self, task_id: int):
        if task_id not in self._dict:
            raise NotFound()
        self._dict.pop(task_id)


class NotFound(Exception):
    """ID not found"""
