import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func

from sqlalchemy.orm import relationship

from db import Base


class Expence(Base):
    __tablename__ = "Expence"
    id = Column(Integer, primary_key=True,autoincrement=True)
    money = Column(Float(),nullable=True)
    type = Column(String(30),nullable=False)
    comment = Column(Text,nullable=True)
    status = Column(Boolean,nullable=True,default=True)
    date = Column(DateTime,default=func.now(), nullable=False)
