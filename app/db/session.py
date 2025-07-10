import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

#환경 변수에 저장된 DB 정보로 database 연결
DATABASE_URL = f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"


engine = create_engine(DATABASE_URL, pool_pre_ping=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)