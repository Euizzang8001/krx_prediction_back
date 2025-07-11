from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from app.core.config import settings
import certifi

#SSL, TLS 인증서 검증을 위한 certifi 추가
ca = certifi.where()
#mongo db 연결
uri = f'mongodb+srv://{settings.MONGO_USER}:{settings.MONGO_PASSWORD}@{settings.MONGO_NAME}.{settings.MONGO_URL}/?retryWrites=true&w=majority&appName={settings.MONGO_NAME}'

#mongodb client 객체 선언 + certifi.where 값 추가하여 연결
Client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=ca)
#연결 성공 or 에러 시 문구 발생하게
try:
    Client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)