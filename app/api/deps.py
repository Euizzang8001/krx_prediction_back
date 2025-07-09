from app.db.session import Session
from app.db.mongo import Client
from typing import Generator

#postgresql 연결 의존성 설정
def get_db() -> Generator:
    db = Session()
    try:
        yield db
    finally:
        db.close()

#mongodb 연결 의존성 설정
def get_mongodb() -> Generator:
    mongo_db = Client
    try:
        yield mongo_db
    finally:
        mongo_db.close()
