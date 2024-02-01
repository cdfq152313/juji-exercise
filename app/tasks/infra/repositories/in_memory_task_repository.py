from app.tasks.entities.task_entity import TaskEntity
from app.tasks.repositories.task_repository import TaskRepository


class InMemoryTaskRepository(TaskRepository):
    def __init__(self):
        self._counter = 0
        self._dict: [int, TaskEntity] = {
            0: TaskEntity(id=0, text='hello', status=True),
        }

    def get_all(self):
        return sorted(self._dict.values(), key=lambda task_entity: task_entity.id)
