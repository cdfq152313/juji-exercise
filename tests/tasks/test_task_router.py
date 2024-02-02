from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.headers.get("Content-Type") == "application/json"
    assert response.json() == {
        "result": [
            {"id": 0, "text": "hello", "status": 1}
        ]
    }
