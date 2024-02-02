from app.tasks.entities.task_entity import TaskEntity


class TaskRepository:
    def get_all(self) -> list[TaskEntity]:
        pass

    def add(self, text: str) -> TaskEntity:
        pass

    def update(self, obj: TaskEntity):
        pass

    def delete(self, id: int):
        pass
