from fastapi import HTTPException
from sqlalchemy.orm import joinedload
from functions.basement import basement_sab
from functions.order import one_order
from functions.products import one_product
from models.order import Orders
from models.products import Products
from models.trade import Trades

def all_trades(search, order_id, product_id, status, db, trade):
    if search:
        trade = trade.filter(Trades.id.like(search)|
                             Trades.model.like(search))

    if order_id:
        trade = trade.filter(Trades.order_id == order_id)

    if product_id:
        trade = trade.filter(Trades.product_id == product_id)

    if status==True:
        status_filter = Trades.status==status
    elif status==False:
        status_filter = Trades.status == status
    else:
        status_filter = Trades.id>0
    trade = db.query(Trades).options(joinedload(Trades.product)).filter(status_filter).all()
    products = db.query(Trades).options(joinedload(Trades.order)).filter(status_filter).all()
    return products, trade


def add_trades(form, db):
    order = db.query(Orders).filter(Orders.id == form.order_id).all()
    if not order:
        raise HTTPException(status_code=400, detail="Bunday raqamli order mavjud emas.")

    product = db.query(Products).filter(Products.id == form.product_id).all()
    if not product:
        raise HTTPException(status_code=400, detail="Bunday raqamli product mavjud emas.")

    new_trade = Trades(
        product_id=form.product_id,
        order_id=form.order_id,
        number=form.number,
        name=form.name,
    )
    db.add(new_trade)
    db.commit()
    db.refresh(new_trade)
    basement_sab(name=form.name, number=form.number, db=db)
    return {"data": "Trade saved"}


def update_trade(id, form, db):
    if one_order(id=form.id, db=db) is None:
        raise HTTPException(status_code=400, detail="Bunday id raqamli order mavjud emas")

    if one_product(id=form.product_id, db=db) is None:
        raise HTTPException(status_code=400, detail="Bunday id raqamli product mavjud emas")

    db.query(Trades).filter(Trades.id == id).update({
        Trades.name: form.name,
        Trades.product_id: form.product_id,
        Trades.order_id: form.order_id,
        Trades.number: form.number,
        # Trades.model: form.model,
        Trades.status: form.status,
    })
    db.commit()


def delete_trade(id, db):
    db.query(Trades).filter(Trades.id == id).update({
        Trades.status: False
    })
    db.commit()
    return {"data": "Malumot o'chirildi"}
