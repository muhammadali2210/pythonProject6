import datetime

from sqlalchemy import Column, Integer, String, Boolean, Float, Text, ForeignKey, Date, DateTime, func
from sqlalchemy.orm import relationship

from db import Base




class Orders(Base):
    __tablename__ = "Orders"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("Customers.id"), nullable=True)
    money = Column(Float, nullable=True, default=0)
    type = Column(String(50), nullable=True)
    loan = Column(Float, nullable=True)
    rest_money = Column(Float, nullable=True)
    deadline = Column(Date,nullable=True)
    status = Column(Boolean, nullable=True, default=True)
    date = Column(DateTime(timezone=True), default=func.now(), nullable=False)

    customer = relationship("Customers", back_populates="order")
    trade = relationship("Trades", back_populates="order")
    income = relationship("Income", back_populates="order")

