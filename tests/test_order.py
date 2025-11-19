import logging
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

logging.basicConfig(level=logging.INFO)

def test_create_order():
    res = client.post("/orders", json={"user_id":"1","product_id":"2","quantity":3})
    assert res.status_code == 200
    logging.info("✅ test_create_order successful")

def test_get_orders():
    res = client.get("/orders")
    assert res.status_code == 200
    logging.info("✅ test_get_orders successful")

def test_get_order_by_id():
    o = client.post("/orders", json={"user_id":"4","product_id":"5","quantity":1}).json()
    res = client.get(f"/orders/{o['id']}")
    assert res.status_code == 200
    logging.info("✅ test_get_order_by_id successful")

def test_update_order():
    o = client.post("/orders", json={"user_id":"7","product_id":"8","quantity":2}).json()
    res = client.put(f"/orders/{o['id']}", json={"user_id":"7","product_id":"8","quantity":5})
    assert res.status_code == 200
    logging.info("✅ test_update_order successful")

def test_delete_order():
    o = client.post("/orders", json={"user_id":"9","product_id":"10","quantity":1}).json()
    res = client.delete(f"/orders/{o['id']}")
    assert res.status_code == 200
    logging.info("✅ test_delete_order successful")
