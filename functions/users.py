from fastapi import HTTPException

from models.users import Users
from routes.auth import get_password_hash
def all_users(db,status):
    if status==True:
        status_filter = Users.status==status
    elif status==False:
        status_filter =Users.status==status
    else:
        status_filter = Users.id>=0

    users = db.query(Users).filter(Users.id>=0).all()
    return users


def add_users(form,db):
    user = db.query(Users).filter(Users.username==form.username).all()
    if user:
        raise HTTPException(status_code=400,detail="Bunday username mavjud qayta kiriting !")
    new_user=Users(name=form.name,
                   roll=form.roll,
                   last_name=form.last_name,
                   number=form.number,
                   username=form.username,
                   password=get_password_hash(form.password)
                   )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return{"data" : "User add base"}

def update_users(id,form,db):
    if one_user(id=form.id,db=db) is None:
        raise HTTPException(status_code=400,detail="Bunday raqamli user mavjud emas qayta urining")
    db.query(Users).filter(Users.id==id).update({
        Users.name:form.name,
        Users.last_name:form.last_name,
        Users.roll:form.roll,
        Users.username:form.username,
        Users.password:form.password,
        Users.number:form.number,
        Users.status:form.status,

    })
    db.commit()



def one_user(id,db):
    return db.query(Users).filter(Users.id==id).first()

def delete_users(id,db):
    db.query(Users).filter(Users.id==id).update({
        Users.status:False
    })

    db.commit()
    return {"data":"Malumot o'chirildi"}
