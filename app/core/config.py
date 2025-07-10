from dotenv import load_dotenv
from pydantic import BaseSettings
import os

#env파일 가져오기
load_dotenv()

#환경 변수를 Settings로 관리
class Settings(BaseSettings):
    #Postgresql 관련 DB 환경 변수
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")

    #MongoDB 관련 환경 변수
    MONGO_USER: str = os.getenv("MONGO_USER")
    MONGO_PASSWORD: str = os.getenv("MONGO_PASSWORD")
    MONGO_URL: str = os.getenv("MONGO_URL")
    MONGO_NAME: str = os.getenv("MONGO_NAME")

    #env파일에서 환경 변수 로드
    class Config:
        env_file = ".env"


#settings로 내보내기
settings = Settings()