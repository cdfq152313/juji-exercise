from dependency_injector import containers, providers

from app.tasks.infra.repositories.in_memory_task_repository import InMemoryTaskRepository
from app.tasks.task_service import TaskService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[".tasks.task_router"]
    )

    task_repository = providers.Singleton(InMemoryTaskRepository)
    task_service = providers.Singleton(
        TaskService,
        repository=task_repository
    )
