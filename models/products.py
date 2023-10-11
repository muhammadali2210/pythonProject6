import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func

from sqlalchemy.orm import relationship

from db import Base


class Products(Base):
    __tablename__ = "Products"
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(30), nullable=True)
    model = Column(String(30), nullable=True)
    number = Column(Float(), nullable=True)
    real_price = Column(Float, nullable = True)
    trade_price = Column(Float, nullable = True)
    description = Column(Text,nullable=True)
    status = Column(Boolean, nullable = True ,default=True)
    date = Column(Date,nullable=True,default=func.now())

    trade = relationship("Trades", back_populates="product")


