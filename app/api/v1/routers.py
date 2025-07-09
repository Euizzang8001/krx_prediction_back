from fastapi import APIRouter
from app.api.v1.endpoints import krx

api_router = APIRouter() #default router 설정

#endpoints에 정의한 krx api를 추가
api_router.include_router(krx.router, tags=["krx"])