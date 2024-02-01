from app.tasks.repositories.task_repository import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository):
        self._repository = repository

    def get_tasks(self):
        return self._repository.get_all()
