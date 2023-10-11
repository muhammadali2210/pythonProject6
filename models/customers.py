import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func

from sqlalchemy.orm import relationship

from db import Base


class Customers(Base):
    __tablename__ = "Customers"
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(30), nullable=True)
    last_name = Column(String(30), nullable=True)
    address = Column(String(100),nullable =True)
    number = Column(String(30), primary_key=False)
    status = Column(Boolean, nullable=True,default=True)
    date = Column(Date,nullable=True,default=func.now())

    order = relationship("Orders", back_populates="customer")



