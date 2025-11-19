from fastapi import APIRouter
from app.models import Order
from app.services import crud_create, crud_read_all, crud_read_one, crud_update, crud_delete

db_orders = {}

router = APIRouter()

@router.post("/orders")
def create_order(o: Order): return crud_create(db_orders, o)

@router.get("/orders")
def get_orders(): return crud_read_all(db_orders)

@router.get("/orders/{id}")
def get_order(id: str): return crud_read_one(db_orders, id)

@router.put("/orders/{id}")
def update_order(id: str, o: Order): return crud_update(db_orders, id, o)

@router.delete("/orders/{id}")
def delete_order(id: str): return crud_delete(db_orders, id)