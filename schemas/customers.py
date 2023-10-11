from pydantic import BaseModel
from typing import Optional

class CustomerBase(BaseModel):
    name:str
    last_name: Optional[str]=None
    address:str
    number:str

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    id:int
    status:bool