from sqlalchemy import Column, Integer, String, Text
from infraestructure.db import Base

class ReviewModel(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    imdb_id = Column(String(20), index=True, nullable=False)
    user_opinion = Column(Text, nullable=False)
    user_rating = Column(Integer, nullable=False)
