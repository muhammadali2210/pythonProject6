import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func

from sqlalchemy.orm import relationship

from db import Base


class Income(Base):
    __tablename__ = "Income"
    id = Column(Integer, primary_key=True,autoincrement=True)
    money = Column(Float(),nullable=True)
    type = Column(String(30),nullable=False)
    orders_id = Column(Integer,ForeignKey("Orders.id"),nullable=False)
    status = Column(Boolean,nullable=True)
    date = Column(DateTime,default=func.now(), nullable=False)


    order = relationship("Orders",back_populates="income")

