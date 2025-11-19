from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_create_order():
    res = client.post("/orders", json={"user_id":"1","product_id":"2","quantity":3})
    assert res.status_code == 200

def test_get_orders():
    res = client.get("/orders")
    assert res.status_code == 200

def test_get_order_by_id():
    o = client.post("/orders", json={"user_id":"4","product_id":"5","quantity":1}).json()
    res = client.get(f"/orders/{o['id']}")
    assert res.status_code == 200

def test_update_order():
    o = client.post("/orders", json={"user_id":"7","product_id":"8","quantity":2}).json()
    res = client.put(f"/orders/{o['id']}", json={"user_id":"7","product_id":"8","quantity":5})
    assert res.status_code == 200
