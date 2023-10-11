from fastapi import HTTPException
from utils.pagination import pagination
from functions.order import one_order
from functions.balance import balance_adding
from models.income import Income
def all_income(search,orders_id,from_date,end_date,page,limit,db,status):
    income = db.query(Income).filter(Income.id >= 0)
    if search:
        income = income.filter(Income.money.like(search) |
                               Income.date.like(search) |
                               Income.type.like(search))

    if orders_id:
        income = income.filter(Income.orders_id == orders_id)
    if from_date and end_date:
        income = income.filter(Income.date>=from_date,Income.date<=end_date)

    if status == True:
        income = income.filter(Income.status == status)
    elif status == False:
        income = income.filter(Income.status == status)
    else:
        income = income.filter(Income.id >= 0)
    return pagination(income, page, limit)

def one_income(id,db):
    return db.query(Income).filter(Income.id==id).first()


def add_income(form,db):
    if one_order(id=form.orders_id, db=db) is None:
        raise HTTPException(status_code=400, detail="Bunday raqamli orders mavjud emas !")

    new_income=Income(
                   orders_id=form.orders_id,
                   money=form.money,
                   type=form.type,

                   )
    db.add(new_income)
    db.commit()
    db.refresh(new_income)
    balance_adding(type=form.type,money=form.money,db=db)
    return{"data" : "User add base"}

def update_income(id,form,db):
    if one_income(id=form.id,db=db) is None:
        raise HTTPException(status_code=400,detail="Bunday id raqamli income mavjud emas")


    db.query(Income).filter(Income.id==id).update({
        Income.money:form.money,
        Income.type:form.type,
        Income.date:form.date,
        Income.status: form.status,
        Income.orders_id: form.orders_id,

    })
    db.commit()

def delete_income(id,db):
    db.query(Income).filter(Income.id==id).update({
        Income.status:False
    })

    db.commit()
    return {"data":"Malumot o'chirildi"}

