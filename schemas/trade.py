from typing import Any

from pydantic import BaseModel


class TradeBase(BaseModel):
    name:str
    product_id: int
    order_id: int
    number:float
    # model: str



class TradeCreate(TradeBase):

    pass


class TradeUpdate(TradeBase):
    id: int
    status: bool
