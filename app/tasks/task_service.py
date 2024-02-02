from app.tasks.entities.task_entity import TaskEntity
from app.tasks.repositories.task_repository import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository):
        self._repository = repository

    def get_tasks(self) -> list[TaskEntity]:
        return self._repository.get_all()

    def create_task(self, text: str) -> TaskEntity:
        return self._repository.add(text)

    def update_task(self, task: TaskEntity) -> TaskEntity:
        return self._repository.update(task)

    def delete_task(self, task_id: int):
        self._repository.delete(task_id)
