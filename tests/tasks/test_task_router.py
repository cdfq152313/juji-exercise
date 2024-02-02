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
    task = {
        "id": r1.json()["result"]["id"],
        "text": "hell word",
        "status": 1,
    }
    r2 = client.put("/task", json=task)
    assert r2.status_code == 200
    assert r2.headers.get("Content-Type") == "application/json"
    assert r2.json() == {"result": task}


def test_delete_task():
    r1 = client.post("/task", json={"text": "hello world"})
    r2 = client.delete(f'/task/{r1.json()["result"]["id"]}')
    assert r2.status_code == 200
    assert r2.headers.get("Content-Type") == "application/json"
