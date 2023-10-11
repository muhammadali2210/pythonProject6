import datetime

from sqlalchemy import Column, Integer, String, Boolean, Float, Text, ForeignKey, Date, DateTime, func
from sqlalchemy.orm import relationship

from db import Base




class Trades(Base):
    __tablename__ = "Trade"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("Products.id"), nullable=False)
    name = Column(String(30), nullable=True)
    # model = Column(String(30), nullable=True)
    number = Column(Float(), nullable=True)
    order_id = Column(Integer, ForeignKey("Orders.id"), nullable=False)
    status = Column(Boolean, nullable=True, default=True)
    date = Column(DateTime, default=func.now(), nullable=False)

    product = relationship("Products", back_populates="trade")
    order = relationship("Orders", back_populates="trade")
