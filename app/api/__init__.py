from fastapi import APIRouter

from .category import router as category_router
from .order import router as order_router
from .product import router as product_router
from .user import router as user_router

api = APIRouter()

api.include_router(user_router, tags=["users"])
api.include_router(product_router, tags=["products"])
api.include_router(order_router, tags=["orders"])
api.include_router(category_router, tags=["categories"])

__all__ = ["api"]