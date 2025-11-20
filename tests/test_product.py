import logging
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

logging.basicConfig(level=logging.INFO)

def test_create_product():
    res = client.post("/products", json={"name": "X", "price": -10})
    assert res.status_code == 200
    logging.info("✅ test_create_product successful")

def test_get_products():
    res = client.get("/products")
    assert res.status_code == 200
    logging.info("✅ test_get_products successful")

def test_get_product_by_id():
    p = client.post("/products", json={"name": "Y", "price": 20}).json()
    res = client.get(f"/products/{p['id']}")
    assert res.status_code == 200
    logging.info("✅ test_get_product_by_id successful")

def test_update_product():
    p = client.post("/products", json={"name": "Z", "price": 30}).json()
    res = client.put(f"/products/{p['id']}", json={"name": "Z2", "price": 35})
    assert res.status_code == 200
    logging.info("✅ test_update_product successful")

def test_delete_product():
    p = client.post("/products", json={"name": "DeleteMe", "price": 50}).json()
    res = client.delete(f"/products/{p['id']}")
    assert res.status_code == 200
    logging.info("✅ test_delete_product successful")
