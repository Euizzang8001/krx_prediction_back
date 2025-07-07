from fastapi import APIRouter
from app.api.v1.endpoints import krx

api_router = APIRouter()
api_router.include_router(krx.router, tags=["krx"])