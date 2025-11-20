import logging
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

logging.basicConfig(level=logging.INFO)

def test_create_category():
    res = client.post("/categories", json={"name": 0})
    assert res.status_code == 200, "failed"
    logging.info("✅ test_create_category successful")

def test_get_categories():
    res = client.get("/categories")
    assert res.status_code == 200
    logging.info("✅ test_get_categories successful")

def test_get_category_by_id():
    c = client.post("/categories", json={"name": "Gaming"}).json()
    res = client.get(f"/categories/{c['id']}")
    assert res.status_code == 200
    logging.info("✅ test_get_category_by_id successful")

def test_update_category():
    c = client.post("/categories", json={"name": "Books"}).json()
    res = client.put(f"/categories/{c['id']}", json={"name": "Books2"})
    assert res.status_code == 200
    logging.info("✅ test_update_category successful")

def test_delete_category_by_id():
    c = client.post("/categories", json={"name": "Music"}).json()
    res = client.delete(f"/categories/{c['id']}")
    assert res.status_code == 200
    logging.info("✅ test_delete_category_by_id successful")
