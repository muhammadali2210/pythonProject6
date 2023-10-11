from fastapi import APIRouter, Depends, HTTPException


from db import Base, engine, get_db

from sqlalchemy.orm import Session

from routes.auth import get_current_active_user


from functions.trade import all_trades, add_trades, update_trade, delete_trade
from schemas.users import UserCurrent

Base.metadata.create_all(bind=engine)


from schemas.trade import *

router_trade = APIRouter()


@router_trade.post('/add')
def add_black_list(form: TradeCreate, db: Session = Depends(get_db), current_user: UserCurrent = Depends(
    get_current_active_user)):
    if add_trades(form=form, db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@router_trade.get('/', status_code=200)
def get_black_lists(seachr:int=0,order_id:int=0,product_id:int=0,status:bool = None,db: Session = Depends(get_db),
                current_user: UserCurrent = Depends(get_current_active_user)):

        return all_trades(search=seachr,order_id=order_id,product_id=product_id,db=db,status=status)




@router_trade.put('/update')
def black_list_update(form: TradeUpdate, db: Session = Depends(get_db),
                      current_user: UserCurrent = Depends(get_current_active_user)):
    if update_trade(id=form.id,form=form, db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")

@router_trade.delete('/delete')
def trade_delete(id: int, db: Session = Depends(get_db),
                    current_user: UserCurrent = Depends(get_current_active_user)):
    return delete_trade(id=id, db=db)


