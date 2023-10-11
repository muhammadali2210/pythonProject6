from fastapi import HTTPException
from sqlalchemy.orm import joinedload

from functions.customers import one_customer
from models.customers import Customers
from models.order import Orders


def all_orders(db,status):
    if status==True:
        status_filter = Orders.status==status
    elif status==False:
        status_filter = Orders.status == status
    else:
        status_filter = Orders.id>=0
    orders = db.query(Customers).options(joinedload(Customers.order)).filter(status_filter).all()
    return orders


def one_order(id, db):
    return db.query(Orders).filter(Orders.id == id).first()


def add_orders(form, db):
    if one_customer(id=form.customer_id, db=db) is None:
        raise HTTPException(status_code=400, detail="Bunday id raqamli customer mavjud emas")
    customer = db.query(Customers).filter(Customers.id == form.customer_id).all()
    if not customer:
        raise HTTPException(status_code=400, detail="Bunday raqamli customer mavjud emas.")

    new_order = Orders(
        customer_id=form.customer_id,
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return {"data": "Order saved"}


def update_order(id, form, db):
    if one_order(id=form.id, db=db) is None:
        raise HTTPException(status_code=400, detail="Bunday id raqamli order mavjud emas")

    if one_customer(id=form.customer_id, db=db) is None:
        raise HTTPException(status_code=400, detail="Bunday id raqamli customer mavjud emas")

    db.query(Orders).filter(Orders.id == id).update({
        Orders.customer_id: form.customer_id,
        Orders.money: form.money,
        Orders.type: form.type,
        Orders.loan: form.loan,
        Orders.rest_money: form.rest_money,
        Orders.deadline: form.deadline,
        Orders.status: form.status
    })
    db.commit()

def delete_order(id, db):
    db.query(Orders).filter(Orders.id == id).update({
        Orders.status: False
    })
    db.commit()
    return {"data": "Malumot o'chirildi"}

