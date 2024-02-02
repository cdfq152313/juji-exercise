from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.headers.get("Content-Type") == "application/json"
    assert response.json() == {"result": []}


def test_create_task():
    text = "hello world"
    response = client.post("/task", json={"text": text})
    assert response.status_code == 201
    assert response.headers.get("Content-Type") == "application/json"
    assert response.json()["result"]["text"] == text
    assert response.json()["result"]["status"] == 0


def test_update_task():
    r1 = client.post("/task", json={"text": "hello world"})
    task_id = r1.json()["result"]["id"]
    task = {
        "id": task_id,
        "text": "hell word",
        "status": 1,
    }
    r2 = client.put(f"/task/{task_id}", json=task)
    assert r2.status_code == 200
    assert r2.headers.get("Content-Type") == "application/json"
    assert r2.json() == {"result": task}


def test_update_task_with_different_task_id():
    task = {
        "id": 3310,
        "text": "hello world",
        "status": 1,
    }
    response = client.put(f"/task/{9527}", json=task)
    assert response.status_code == 400
    assert response.headers.get("Content-Type") == "application/json"


def test_update_not_exist_task():
    task_id = 3310
    task = {
        "id": task_id,
        "text": "hello world",
        "status": 1,
    }
    response = client.put(f"/task/{task_id}", json=task)
    assert response.status_code == 404
    assert response.headers.get("Content-Type") == "application/json"


def test_delete_task():
    r1 = client.post("/task", json={"text": "hello world"})
    r2 = client.delete(f'/task/{r1.json()["result"]["id"]}')
    assert r2.status_code == 200
    assert r2.headers.get("Content-Type") == "application/json"


def test_delete_not_exist_task():
    response = client.delete(f"/task/3310")
    assert response.status_code == 404
    assert response.headers.get("Content-Type") == "application/json"
