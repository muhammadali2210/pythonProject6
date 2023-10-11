from fastapi import APIRouter,Depends,HTTPException
from pydantic.datetime_parse import date

from db import Base,engine,get_db

from sqlalchemy.orm import Session

from routes.auth import get_current_active_user
from schemas.users import UserCurrent

Base.metadata.create_all(bind=engine)
from functions.balance import add_balance, all_balance, update_balance, delete_balance
from schemas.balance import *

router_balance = APIRouter()

@router_balance.post('/add')
def balance_add(form:BalanceCreate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if add_balance(form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")


@router_balance.get('/',status_code=200)
def get_balans(search:str=None,from_date:str=None,end_date:str=None,page:int=1,limit:int=5,status:bool=None,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

        return all_balance(search=search,page=page,limit=limit,db=db,status=status,from_date=from_date,end_date=end_date)



@router_balance.put('/update',)
def balance_update(form:BalanceUpdate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if update_balance(id=form.id,form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")

@router_balance.delete('/del',)
def balance_delete(id:int,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):
    return delete_balance(id=id,db=db)
