import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

#환경 변수 가져오기
load_dotenv()

#환경 변수에 저장된 DB 정보로 database 연결
db_user = os.getenv("DB_USER")
DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"


engine = create_engine(DATABASE_URL, pool_pre_ping=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)