from fastapi import APIRouter, Depends, HTTPException
from app.api.deps import get_db, get_mongodb
from app.schemas.krx import prediction, closing, news
from typing import List
from sqlalchemy.orm import Session
from pymongo.mongo_client import MongoClient
from datetime import datetime, timedelta
import pendulum
from app.models.krx import Stock
from bson import json_util
from fastapi.responses import JSONResponse

router = APIRouter()

#종목 별로 가장 최근 날짜의 종가, 가장 최근 날짜로 예측한 예측 변화율과 예측 종가 get하기
@router.get("/krx_prediction/{stock_name}")
async def get_krx_prediction(stock_name: str, db: Session = Depends(get_db)):
    #오늘 날짜 가져오기
    today = datetime.now()
    #장 마감 이전이라면, 가장 최근의 마감된 장에 해당하는 날짜 찾기
    if today.hour < 15 or (today.hour == 15 and today.minute < 30):
        today -=timedelta(days=1)
    while today.weekday() > 5:
        today -= timedelta(days=1)

    #가장 최근 종가와 그 정보를 바탕으로 예측한 종가 변화율과 예측 종가 가져와 response
    closing, predicted_closing_ratio, predicted_closing = db.query(Stock.closing, Stock.predicted_closing_ratio, Stock.predicted_closing).filter(
        Stock.name == stock_name, Stock.date == today.strftime("%Y%m%d")
    ).first()

    return {
    "closing": closing,
    "predicted_closing_ratio": predicted_closing_ratio,
    "predicted_closing": predicted_closing
    }

#종목 별로 종가의 변화를 dataframe 형식으로 return
@router.get("/krx_closing/{stock_name}")
async def get_krx_closing(stock_name: str, db: Session = Depends(get_db)):
    #해당 종목의 종가 및 예측 종가 가져오기
    results = db.query(Stock.date,Stock.closing).filter(
        Stock.name == stock_name
    ).all()

    #날짜와 종가 구분하여 response로 return
    date_list = []
    closing_list = []

    for date, closing in results:
        date_list.append(date)
        closing_list.append(closing)
    return {
        "date": date_list,
        "closing": closing_list
    }

#반도체 관련 종목의 실시간 뉴스 url을 return
@router.get("/news")
async def get_news(client: MongoClient = Depends(get_mongodb)):
    #news를 저장한 DB에 연결
    database = client['news_db']
    #현재 시간을 받아 현재 시간부터 1시간 전 사이에 출간된 뉴스들 가져오기
    now = pendulum.now()
    col_name = now.strftime("%Y-%m-%d %H")
    collection = database[col_name]
    results = collection.find({}, {'_id': False})

    #json화하여 Response로 return
    return JSONResponse(content=json_util.loads(json_util.dumps(results)))

#해당 종목의 모델의 예측값과 실제 값을 return
@router.get("/model_history/{stock_name}")
async def get_model_history(stock_name: str):
    return
