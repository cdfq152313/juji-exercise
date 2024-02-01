from .task_entity import TaskEntity


class TaskService:
    def get_tasks(self):
        return [
            TaskEntity(id=0, text='hello', status=True),
        ]
