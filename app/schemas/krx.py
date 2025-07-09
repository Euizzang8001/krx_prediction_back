from pydantic import BaseModel

class closing(BaseModel):
    date: str
    closing: float

class prediction(BaseModel):
    date: str
    closing: float
    predicted_closing_change_ratio: float
    predicted_closing_change: float

class news(BaseModel):
    title: str
    description: str
    url: str