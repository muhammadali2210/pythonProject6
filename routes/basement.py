from fastapi import APIRouter,Depends,HTTPException
from pydantic.datetime_parse import date

from db import Base,engine,get_db

from sqlalchemy.orm import Session

from routes.auth import get_current_active_user
from schemas.users import UserCurrent

Base.metadata.create_all(bind=engine)
from functions.basement import add_basement, all_basement, update_basement, delete_basement
from schemas.basement import *

router_basement = APIRouter()

@router_basement.post('/add')
def basement_add(form:BasementCreate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if add_basement(form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")


@router_basement.get('/',status_code=200)
def get_basement(search:str=None,user_id:int=0,from_date:str=None,end_date:str=None,page:int=1,limit:int=5,status:bool=None,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

        return all_basement(search=search,user_id=user_id,page=page,limit=limit,db=db,status=status,from_date=from_date,end_date=end_date)



@router_basement.put('/update',)
def basement_update(form:BasementUpdate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if update_basement(id=form.id,form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")

@router_basement.delete('/del',)
def basement_delete(id:int,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):
    return delete_basement(id=id,db=db)
