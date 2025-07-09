from fastapi import FastAPI
from app.api.v1.routers import api_router

#app 정보 설정
app = FastAPI(
    title="krx prediction server",
    description="Krx prediction server",
    version="1.0.0",
)

#api내에 정의된 모든 api를 등록
app.include_router(api_router, prefix="/api/v1")

#default api 설정
@app.get("/")
def root():
    return {"message": "Hello KRX!"}