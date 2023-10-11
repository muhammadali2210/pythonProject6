from fastapi import HTTPException
from sqlalchemy.orm import joinedload
from utils.pagination import pagination
from models.balance import Balance
from routes.auth import get_password_hash
def all_balance(search,from_date,end_date,page,limit,db,status):
    balance = db.query(Balance).filter(Balance.id >= 0)
    if search:
        balance = balance.filter(Balance.money.like(search) |
                               Balance.type.like(search) |
                               Balance.status.like(search)|
                               Balance.date.like(search))

    if from_date and end_date:
        balance = balance.filter(Balance.date>=from_date,Balance.date<=end_date)

    if status == True:
        balance = balance.filter(Balance.status == status)
    if status == False:
        balance = balance.filter(Balance.status == status)
    else:
        balance = balance.filter(Balance.id >= 0)
    return pagination(balance, page, limit)

def one_balance(id,db):
    return db.query(Balance).filter(Balance.id==id).first()


def add_balance(form,db):
    new_orders=Balance(
                   money=form.money,
                   type=form.type,
                   )
    db.add(new_orders)
    db.commit()
    db.refresh(new_orders)

    return{"data" : "User add base"}

def update_balance(id,form,db):
    if one_balance(id=form.id,db=db) is None:
        raise HTTPException(status_code=400,detail="Bunday id raqamli balance mavjud emas")
    db.query(Balance).filter(Balance.id==id).update({
        Balance.money:form.money,
        Balance.type:form.type,
        Balance.status: form.status,

    })
    db.commit()

def delete_balance(id,db):
    db.query(Balance).filter(Balance.id==id).update({
        Balance.status:False
    })

    db.commit()
    return {"data":"Malumot o'chirildi"}

def balance_adding(type,money,db):
    balance = db.query(Balance).filter(Balance.type==type).first()
    new_money = balance.money + money
    db.query(Balance).filter(Balance.type==type).update({
        Balance.money:new_money
    })
    db.commit()

def balance_sab(type,money,db):
    balance = db.query(Balance).filter(Balance.type==type).first()
    new_money = balance.money - money
    db.query(Balance).filter(Balance.type==type).update({
        Balance.money:new_money
    })
    db.commit()


