from app.db.session import Session
from app.db.mongo import Client
from typing import Generator

def get_db() -> Generator:
    db = Session()
    try:
        yield db
    finally:
        db.close()

def get_mongodb() -> Generator:
    mongo_db = Client
    try:
        yield mongo_db
    finally:
        mongo_db.close()
