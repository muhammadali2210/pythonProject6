from fastapi import HTTPException
from sqlalchemy.orm import joinedload
from utils.pagination import pagination
from functions.users import one_user
from models.basement import Basement
from models.users import Users
from routes.auth import get_password_hash
def all_basement(search,user_id,from_date,end_date,page,limit,db,status):
    basement = db.query(Basement).filter(Basement.id >= 0)
    if search:
        basement = basement.filter(Basement.trade_price.like(search) |
                               Basement.real_price.like(search) |
                               Basement.number.like(search)|
                               Basement.name.like(search)|
                               Basement.barcode.like(search) |
                               Basement.measure.like(search))

    if user_id:
        basement = basement.filter(Basement.user_id == user_id)

    if from_date and end_date:
        basement = basement.filter(Basement.date>=from_date,Basement.date<=end_date)

    if status == True:
        basement = basement.filter(Basement.status == status)
    if status == False:
        basement = basement.filter(Basement.status == status)
    else:
        basement = basement.filter(Basement.id >= 0)

    users = db.query(Basement).options(joinedload(Basement.users)).all()
    return pagination(basement, page, limit),users

def one_basement(id,db):
    return db.query(Basement).filter(Basement.id==id).first()


def add_basement(form,db):
    new_basements=Basement(
                   name = form.name,
                   real_price = form.real_price,
                   trade_price = form.trade_price,
                   number = form.number,
                   measure = form.measure,
                   barcode = form.barcode,
                   # user_id = form.user_id

                   )
    db.add(new_basements)
    db.commit()
    db.refresh(new_basements)

    return{"data" : "User add base"}

def update_basement(id,form,db):
    if one_user(id=form.id, db=db) is None:
        raise HTTPException(status_code=400, detail="Bunday id raqamli user mavjud emas")
    if one_basement(id=form.id,db=db) is None:
        raise HTTPException(status_code=400,detail="Bunday id raqamli basement mavjud emas")
    db.query(Basement).filter(Basement.id==id).update({
        Basement.id:form.id,
        Basement.name:form.name,
        Basement.real_price:form.real_price,
        Basement.trade_price:form.trade_price,
        Basement.number:form.number,
        Basement.measure:form.measure,
        Basement.barcode:form.barcode,
        Basement.user_id:form.user_id,
        Basement.date:form.date


    })
    db.commit()

def delete_basement(id,db):
    db.query(Basement).filter(Basement.id==id).update({
        Basement.status:False
    })

    db.commit()
    return {"data":"Malumot o'chirildi"}

# def balance_adding(type,money,db):
#     balance = db.query(Balance).filter(Balance.type==type).first()
#     new_money = balance.money + money
#     db.query(Balance).filter(Balance.type==type).update({
#         Balance.money:new_money
#     })
#     db.commit()
#
# def balance_sab(type,money,db):
#     balance = db.query(Balance).filter(Balance.type==type).first()
#     new_money = balance.money - money
#     db.query(Balance).filter(Balance.type==type).update({
#         Balance.money:new_money
#     })
#     db.commit()


def basement_add(name,number,db):
    basement = db.query(Basement).filter(Basement.name==name).first()
    new_number = basement.number + number
    db.query(Basement).filter(Basement.name==name).update({
        Basement.number:new_number
    })
    db.commit()

def basement_sab(name,number,db):
    basement = db.query(Basement).filter(Basement.name==name).first()
    new_number = basement.number - number
    db.query(Basement).filter(Basement.name==name).update({
        Basement.number:new_number
    })
    db.commit()

