from pydantic import BaseModel
from typing import Optional
from pydantic.datetime_parse import date



class OrderBase(BaseModel):
    customer_id: int

class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderBase):
    money: int
    type: str
    loan: int
    rest_money: int
    deadline: date
    id: int
    status: bool
