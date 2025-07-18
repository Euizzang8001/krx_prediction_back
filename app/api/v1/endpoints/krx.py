from fastapi import APIRouter, Depends, HTTPException
from app.api.deps import get_db, get_mongodb
from sqlalchemy.orm import Session
from sqlalchemy import asc
from pymongo.mongo_client import MongoClient
from datetime import datetime, timedelta
from typing import List
import pendulum
from app.models.krx import Stock
from bson import json_util
from fastapi.responses import JSONResponse

from app.schemas.krx import News, KrxHistory, KrxPrediction

router = APIRouter()

#종목 별로 가장 최근 날짜의 종가, 가장 최근 날짜로 예측한 예측 변화율과 예측 종가 get하기
@router.get("/krx_prediction/{stock_name}")
async def get_krx_prediction(stock_name: str, db: Session = Depends(get_db)) -> KrxPrediction:
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

    return KrxPrediction(
        closing = closing,
        predicted_closing_ratio = predicted_closing_ratio,
        predicted_closing = predicted_closing
    )

#종목 별로 종가 history와 예측 종가 history를 return
@router.get("/krx_closing/{stock_name}")
async def get_krx_closing(stock_name: str, db: Session = Depends(get_db)) -> KrxHistory:
    #해당 종목의 종가 및 예측 종가 가져오기
    results = db.query(
        Stock.date,Stock.closing, Stock.predicted_closing
    ).filter(
        Stock.name == stock_name
    ).order_by(
        asc(Stock.date)
    ).all()

    #날짜, 종가, 예측 종가를 구분한 후, response로 전달
    date_list = []
    closing_list = []
    predicted_closing_list = []

    for date, closing, predicted_closing in results:
        date_list.append(date)
        closing_list.append(closing)
        predicted_closing_list.append(predicted_closing)

    response = KrxHistory(
        date_list = date_list,
        closing_list = closing_list,
        predicted_closing_list=predicted_closing_list
    )
    return response

#반도체 관련 종목의 실시간 뉴스 url을 return
@router.get("/news/{cursor}")
async def get_news(cursor: int, db = Depends(get_mongodb)) -> List[News]:
    #출간시간(pub_time)으로 내림차순 정렬한 후, cursor에 따라 이후 5개의 뉴스만 가져오기
    collection = db['news_collection']
    results = collection.find({}, {'_id': False}).sort("pub_time", -1).skip(cursor).limit(5)
    json_result = json_util.loads(json_util.dumps(results))
    #json화하여 Response로 return
    return json_result