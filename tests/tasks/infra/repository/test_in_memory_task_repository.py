import pytest

from app.tasks.entities.task_entity import TaskEntity
from app.tasks.infra.repositories.in_memory_task_repository import InMemoryTaskRepository, NotFound


@pytest.fixture
def repository() -> InMemoryTaskRepository:
    return InMemoryTaskRepository()


def test_init_must_be_empty(repository: InMemoryTaskRepository):
    x = repository.get_all()
    assert len(x) == 0


def test_create_must_success(repository: InMemoryTaskRepository):
    text = "hello world"
    data = repository.add(text)
    result = repository.get_all()[0]
    assert data == result
    assert data.text == text


def test_update_must_success(repository: InMemoryTaskRepository):
    repository.add("hello world")
    new_data = TaskEntity(id=0, text="hell word", status=True)
    repository.update(new_data)
    result = repository.get_all()[0]
    assert new_data == result


def test_update_not_exist_id(repository: InMemoryTaskRepository):
    with pytest.raises(NotFound):
        data = repository.add("hello world")
        new_data = TaskEntity(id=3310, text="hell word", status=True)
        repository.update(new_data)


def test_delete_must_success(repository: InMemoryTaskRepository):
    data = repository.add("hello world")
    repository.delete(data.id)
    result = repository.get_all()
    assert len(result) == 0


def test_delete_not_exist_id(repository: InMemoryTaskRepository):
    with pytest.raises(NotFound):
        repository.add("hello world")
        repository.delete(3310)
