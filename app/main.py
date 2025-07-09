from fastapi import FastAPI
from app.api.v1.routers import api_router

app = FastAPI(
    title="krx prediction server",
    description="Krx prediction server",
    version="1.0.0",
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Hello KRX!"}