from fastapi import APIRouter

router = APIRouter()

#종목 별로 가장 최근 날짜의 종가, 가장 최근 날짜로 예측한 예측 변화율과 예측 종가 get하기
@router.get("/krx_prediction/{stock_name}")
async def get_krx_prediction(stock_name: str):
    return

#종목 별로 종가의 변화를 dataframe 형식으로 return
@router.get("/krx_closing/{stock_name}")
async def get_krx_closing(stock_name: str):
    return

#반도체 관련 종목의 실시간 뉴스 url을 return
@router.get("/news")
async def get_news(stock_name: str):
    return

#해당 종목의 모델의 예측값과 실제 값을 return
@router.get("/model_history/{stock_name}")
async def get_model_history(stock_name: str):
    return
