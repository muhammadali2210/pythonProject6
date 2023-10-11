import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func

from sqlalchemy.orm import relationship

from db import Base


class Basement(Base):
    __tablename__ = "Basement"
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(30), nullable=True)
    real_price = Column(Float(), nullable=True)
    trade_price = Column(Float(), nullable=True)
    number = Column(Float(), nullable=True)
    measure = Column(String(30), nullable=True)
    barcode = Column(String(30), nullable=True)
    status = Column(Boolean, nullable=True,default=True)
    date = Column(Date,default=func.now(),nullable=False)
    user_id = Column(Integer, ForeignKey("Users.id"), nullable=True)

    users = relationship("Users", back_populates="basement")
