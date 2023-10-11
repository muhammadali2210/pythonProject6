from datetime import date

from pydantic import BaseModel
from typing import Optional

class ExpenceBase(BaseModel):
    money:float
    type:str
    comment:str




class ExpenceCreate(ExpenceBase):
    pass


class ExpenceUpdate(ExpenceBase):
    id:int
    status:bool