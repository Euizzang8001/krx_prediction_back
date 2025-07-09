from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Stock(Base):
    __tablename__ = 'stocks'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(String)
    closing = Column(Float)
    closing_changed_ratio = Column(Float)
    exchanging_change = Column(Float)
    semi_avg_closing_changed_ratio = Column(Float)
    news_score = Column(Float)
    predicted_closing_ratio = Column(Float)
    predicted_closing = Column(Float)
    next_day_closing_change_ratio = Column(Float)
    news_num = Column(Integer)
