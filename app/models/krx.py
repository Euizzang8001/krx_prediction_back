from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

#database와 class로 선언된 table을 mapping해주는 declarative_base객체 선언
Base = declarative_base()

#Stock table 구현
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
