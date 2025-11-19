from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_create_category():
    res = client.post("/categories", json={"name": "Tech"})
    assert res.status_code == 200

def test_get_categories():
    res = client.get("/categories")
    assert res.status_code == 200

def test_get_category_by_id():
    c = client.post("/categories", json={"name": "Gaming"}).json()
    res = client.get(f"/categories/{c['id']}")
    assert res.status_code == 200

def test_update_category():
    c = client.post("/categories", json={"name": "Books"}).json()
    res = client.put(f"/categories/{c['id']}", json={"name": "Books2"})
    assert res.status_code == 200
