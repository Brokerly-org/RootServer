from fastapi import APIRouter

from .endpoints import redirect_router


v1_router = APIRouter()
v1_router.include_router(redirect_router)
