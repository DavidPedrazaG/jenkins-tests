from fastapi import APIRouter
from app.models import Product
from app.services import crud_create, crud_read_all, crud_read_one, crud_update, crud_delete

db_products = {}

router = APIRouter()

@router.post("/products")
def create_product(p: Product): return crud_create(db_products, p)

@router.get("/products")
def get_products(): return crud_read_all(db_products)

@router.get("/products/{id}")
def get_product(id: str): return crud_read_one(db_products, id)

@router.put("/products/{id}")
def update_product(id: str, p: Product): return crud_update(db_products, id, p)

@router.delete("/products/{id}")
def delete_product(id: str): return crud_delete(db_products, id)