from pydantic import BaseModel
from typing import Optional

class BalanceBase(BaseModel):
    money:float
    type:str



class BalanceCreate(BalanceBase):
    pass

class BalanceUpdate(BalanceBase):
    id:int
    status:bool