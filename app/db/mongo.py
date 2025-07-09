from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

#환경변수 가져오기
load_dotenv()

#mongo db 연결
uri = f'mongodb+srv://{os.getenv("MONGO_USER")}:{os.getenv("MONGO_PASSWORD")}@{os.getenv("MONGO_NAME")}.{os.getenv("MONGO_URL")}/?retryWrites=true&w=majority&appName={os.getenv("MONGO_NAME")}'

#mongodb client 객체 선언
Client = MongoClient(uri, server_api=ServerApi('1'))
#연결 성공 or 에러 시 문구 발생하게
try:
    Client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)