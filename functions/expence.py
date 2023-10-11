from fastapi import HTTPException
from sqlalchemy.orm import joinedload
from utils.pagination import pagination
from functions.customers import one_customer
from models.expence import Expence
from routes.auth import get_password_hash
from functions.balance import balance_sab
def all_expence(search,from_date,end_date,page,limit,db,status):
    expence = db.query(Expence).filter(Expence.id >= 0)
    if search:
        expence = expence.filter(Expence.money.like(search) |
                               Expence.date.like(search) |
                               Expence.type.like(search) |
                               Expence.comment.like(search))

    if from_date and end_date:
        expence = expence.filter(Expence.date>=from_date,Expence.date<=end_date)

    if status == True:
        expence = expence.filter(Expence.status == status)
    elif status == False:
        expence = expence.filter(Expence.status == status)
    else:
        expence = expence.filter(Expence.id >= 0)
    return pagination(expence, page, limit)

def one_expence(id,db):
    return db.query(Expence).filter(Expence.id==id).first()


def add_expence(form,db):
    # customer = db.query(Customers).filter(Customers.id == form.customers_id).all()
    # if not customer:
    # raise HTTPException(status_code=400, detail="Bunday raqamli customer mavjud emas !")
    new_expence=Expence(
                   money=form.money,
                   type=form.type,
                   comment=form.comment,

                   )
    db.add(new_expence)
    db.commit()
    db.refresh(new_expence)
    balance_sab(type=form.type,money=form.money,db=db)
    return{"data" : "User add base"}

def update_expence(id,form,db):
    if one_expence(id=form.id,db=db) is None:
        raise HTTPException(status_code=400,detail="Bunday id raqamli order mavjud emas")
    db.query(Expence).filter(Expence.id==id).update({
        Expence.money:form.money,
        Expence.type:form.type,
        Expence.date:form.date,
        Expence.status: form.status,

    })
    db.commit()

def delete_expence(id,db):
    db.query(Expence).filter(Expence.id==id).update({
        Expence.status:False
    })

    db.commit()
    return {"data":"Malumot o'chirildi"}

