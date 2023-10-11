from pydantic import BaseModel
from typing import Optional

class BasementBase(BaseModel):
    name:str
    real_price:float
    trade_price:float
    number:float
    measure:str
    barcode:str





class BasementCreate(BasementBase):
   pass

class BasementUpdate(BasementBase):
    id:int
    user_id:int
    status:bool