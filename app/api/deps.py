from app.db.session import Session
from typing import Generator

def get_db() -> Generator:
    db = Session()
    try:
        yield db
    finally:
        db.close()