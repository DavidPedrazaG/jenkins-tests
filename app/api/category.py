from fastapi import APIRouter
from app.models import Category
from app.services import crud_create, crud_read_all, crud_read_one, crud_update, crud_delete

db_categories = {}

router = APIRouter()

@router.post("/categories")
def create_category(c: Category): return crud_create(db_categories, c)

@router.get("/categories")
def get_categories(): return crud_read_all(db_categories)

@router.get("/categories/{id}")
def get_category(id: str): return crud_read_one(db_categories, id)

@router.put("/categories/{id}")
def update_category(id: str, c: Category): return crud_update(db_categories, id, c)

@router.delete("/categories/{id}")
def delete_category(id: str): return crud_delete(db_categories, id)