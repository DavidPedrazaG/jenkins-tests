from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_create_user():
    res = client.post("/users", json={"name": "A", "email": "a@a.com"})
    assert res.status_code == 200

def test_get_users():
    res = client.get("/users")
    assert res.status_code == 200

def test_get_user_by_id():
    user = client.post("/users", json={"name": "B", "email": "b@b.com"}).json()
    res = client.get(f"/users/{user['id']}")
    assert res.status_code == 200

def test_update_user():
    user = client.post("/users", json={"name": "C", "email": "c@c.com"}).json()
    res = client.put(f"/users/{user['id']}", json={"name": "C2", "email": "c2@c.com"})
    assert res.status_code == 200
