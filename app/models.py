from sqlalchemy import Column, Integer, String, DateTime, func
from .db import Base

class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    score = Column(Integer, nullable=False)
    timestamp = Column(DateTime, server_default=func.now())
