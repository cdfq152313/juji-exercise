from app.tasks.dto.task_resp_dto import TaskRespDto
from app.tasks.repositories.task_repository import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository):
        self._repository = repository

    def get_tasks(self):
        return {
            "result": [
                TaskRespDto(id=task_entity.id, text=task_entity.text, status=1 if task_entity.status else 0)
                for task_entity in self._repository.get_all()
            ]
        }
