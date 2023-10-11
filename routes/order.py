from fastapi import APIRouter, Depends, HTTPException
from pydantic.datetime_parse import date

from db import Base, engine, get_db

from sqlalchemy.orm import Session

from routes.auth import get_current_active_user

from models.order import Orders
from schemas.order import OrderCreate, OrderUpdate
from functions.order import all_orders, add_orders, update_order, delete_order
from schemas.users import UserCurrent

Base.metadata.create_all(bind=engine)


from schemas.order import *

router_order = APIRouter()


@router_order.post('/add')
def add_black_list(form: OrderCreate, db: Session = Depends(get_db), current_user: UserCurrent = Depends(
    get_current_active_user)):
    if add_orders(form=form, db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@router_order.get('/', status_code=200)
def get_black_lists(status:bool = None,db: Session = Depends(get_db),
                current_user: UserCurrent = Depends(get_current_active_user)):

        return all_orders(db=db,status=status)




@router_order.put('/update')
def black_list_update(form: OrderUpdate, db: Session = Depends(get_db),
                      current_user: UserCurrent = Depends(get_current_active_user)):
    if update_order(id=form.id,form=form, db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@router_order.delete('/delete')
def order_delete(id: int, db: Session = Depends(get_db),
                    current_user: UserCurrent = Depends(get_current_active_user)):
    return delete_order(id=id, db=db)

