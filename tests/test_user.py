import logging
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

logging.basicConfig(level=logging.INFO)

def test_create_user():
    res = client.post("/users", json={"name": "A", "email": "a@a.com"})
    assert res.status_code == 200
    logging.info("✅ test_create_user successful")

def test_get_users():
    res = client.get("/users")
    assert res.status_code == 200
    logging.info("✅ test_get_users successful")

def test_get_user_by_id():
    user = client.post("/users", json={"name": "B", "email": "b@b.com"}).json()
    res = client.get(f"/users/{user['id']}")
    assert res.status_code == 200
    logging.info("✅ test_get_user_by_id successful")

def test_update_user():
    user = client.post("/users", json={"name": "C", "email": "c@c.com"}).json()
    res = client.put(f"/users/{user['id']}", json={"name": "C2", "email": "c2@c.com"})
    assert res.status_code == 200
    logging.info("✅ test_update_user successful")

def test_delete_user():
    user = client.post("/users", json={"name": "DeleteMe", "email": "deleteme@a.com"}).json()
    res = client.delete(f"/users/{user['id']}")
    assert res.status_code == 200
    logging.info("✅ test_delete_user successful")
