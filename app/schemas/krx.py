from pydantic import BaseModel
from typing import List

class KrxPrediction(BaseModel):
    closing: float
    predicted_closing_ratio: float
    predicted_closing: float

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "closing": 5.252,
                    "predicted_closing_ratio": 5.252,
                    "predicted_closing": 5.252
                }
            ]
        }
    }

class KrxHistory(BaseModel):
    date_list: List[str]
    closing_list: List[float | None]
    predicted_closing_list: List[float | None]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "date_list": ["20250707", "20250708", "20250709"],
                    "closing_list": [5.252, 5.252, 5.252],
                    "predicted_closing_list": [5.252, 5.252, 5.252]
                }
            ]
        }
    }

class News(BaseModel):
    title: str
    description: str
    url: str
    pub_time: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "마그트론, 중소벤처기업부장관 표창…中 희토류 수출 제한으로 주목",
                    "description": "안준범 마그트론 대표는 “자석은 전기차, <b>반도체</b>, 로봇 등 전략 산업의 핵심 기반 소재이며, 공급망 다변화와 자립…",
                    "url": "https://n.news.naver.com/mnews/article/018/0006055862?sid=105",
                    "pub_time": "2025-07-03 16:56:00"
                }
            ]
        }
    }