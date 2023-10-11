import datetime

from sqlalchemy import Column, Integer, String, Boolean, Float, Text, ForeignKey, Date, DateTime, func
from sqlalchemy.orm import relationship

from db import Base




class Balance(Base):
    __tablename__ = "Balance"
    id = Column(Integer, primary_key=True)
    money = Column(Float(), nullable=True, default=0)
    type = Column(String(50), nullable=False)
    status = Column(Boolean, nullable=True, default=True)
    date = Column(Date(), default=func.now(), nullable=True)