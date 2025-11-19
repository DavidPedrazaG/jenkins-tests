from fastapi import APIRouter
from app.models import User
from app.services import crud_create, crud_read_all, crud_read_one, crud_update, crud_delete

db_users = {}

router = APIRouter()

@router.post("/users")
def create_user(u: User): return crud_create(db_users, u)

@router.get("/users")
def get_users(): return crud_read_all(db_users)

@router.get("/users/{id}")
def get_user(id: str): return crud_read_one(db_users, id)

@router.put("/users/{id}")
def update_user(id: str, u: User): return crud_update(db_users, id, u)

@router.delete("/users/{id}")
def delete_user(id: str): return crud_delete(db_users, id)
