from fastapi import APIRouter,Depends,HTTPException
from pydantic.datetime_parse import date

from db import Base,engine,get_db

from sqlalchemy.orm import Session

from routes.auth import get_current_active_user
from schemas.users import UserCurrent

Base.metadata.create_all(bind=engine)
from functions.expence import add_expence, all_expence, update_expence, delete_expence
from schemas.expence import *

router_expence = APIRouter()

@router_expence.post('/add')
def expence_add(form:ExpenceCreate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if add_expence(form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")


@router_expence.get('/',status_code=200)
def get_expence(search:str=None,from_date:str=None,end_date:str=None,page:int=1,limit:int=5,status:bool=None,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

        return all_expence(search=search,page=page,limit=limit,db=db,status=status,from_date=from_date,end_date=end_date)



@router_expence.put('/update',)
def expence_update(form:ExpenceUpdate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if update_expence(id=form.id,form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")

@router_expence.delete('/del',)
def expence_delete(id:int,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):
    return delete_expence(id=id,db=db)
