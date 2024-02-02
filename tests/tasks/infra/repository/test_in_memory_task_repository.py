import pytest

from app.tasks.infra.repositories.in_memory_task_repository import InMemoryTaskRepository, NotFound


@pytest.fixture
def repository() -> InMemoryTaskRepository:
    return InMemoryTaskRepository()


def test_init_must_be_empty(repository: InMemoryTaskRepository):
    x = repository.get_all()
    assert len(x) == 0


def test_create_must_success(repository: InMemoryTaskRepository):
    data = repository.add("hello world")
    result = repository.get_all()[0]
    assert data == result


def test_update_must_success(repository: InMemoryTaskRepository):
    data = repository.add("hello world")
    copy = data.model_copy(update={"text": "hell word", "status": True})
    repository.update(copy)
    result = repository.get_all()[0]
    assert copy == result


def test_update_not_exist_id(repository: InMemoryTaskRepository):
    with pytest.raises(NotFound):
        data = repository.add("hello world")
        copy = data.model_copy(update={"text": "hell word", "status": True, "id": 3})
        repository.update(copy)


def test_delete_must_success(repository: InMemoryTaskRepository):
    data = repository.add("hello world")
    repository.delete(data.id)
    result = repository.get_all()
    assert len(result) == 0


def test_delete_not_exist_id(repository: InMemoryTaskRepository):
    with pytest.raises(NotFound):
        repository.add("hello world")
        repository.delete(3310)
