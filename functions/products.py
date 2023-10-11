from fastapi import HTTPException
from sqlalchemy.orm import joinedload
from functions.basement import basement_add
from utils.pagination import pagination
from models.products import Products
from routes.auth import get_password_hash
def all_products(search,from_date,end_date,page,limit,db,status):
    products = db.query(Products).filter(Products.id >= 0)
    if search:
        products = products.filter(Products.name.like(search) |
                               Products.money.like(search) |
                               Products.rest_money.like(search) |
                               Products.real_price.like(search)|
                               Products.trade_price.like(search))

    if from_date and end_date:
        products = products.filter(Products.date>=from_date,Products.date<=end_date)

    if status == True:
        products = products.filter(Products.status == status)
    elif status == False:
        products = products.filter(Products.status == status)
    else:
        products = products.filter(Products.id >= 0)
    return pagination(products, page, limit)


def add_products(form,db):
    new_products=Products(
                   name=form.name,
                   model=form.model,
                   number=form.number,
                   real_price=form.real_price,
                   trade_price=form.trade_price,
                   description=form.description,
                   )
    db.add(new_products)
    db.commit()
    db.refresh(new_products)
    basement_add(name=form.name, number=form.number, db=db)
    return{"data" : "User add base"}

def update_products(id,form,db):
    if one_product(id=form.id,db=db) is None:
        raise HTTPException(status_code=400,detail="Bunday raqamli product yo'q")
    db.query(Products).filter(Products.id==id).update({
        Products.name:form.name,
        Products.model:form.model,
        Products.number:form.number,
        Products.real_price:form.real_price,
        Products.trade_price:form.trade_price,
        Products.description:form.description,
        Products.status: form.status,

    })
    db.commit()


def one_product(id,db):
    return db.query(Products).filter(Products.id==id).first()

def delete_products(id,db):
    db.query(Products).filter(Products.id==id).update({
        Products.status:False
    })

    db.commit()
    return {"data":"Malumot o'chirildi"}