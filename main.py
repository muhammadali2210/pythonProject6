from fastapi import FastAPI

from routes import auth, users, customers, products, trade, order, balance, income, expence, basement

from db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Shablon",
    responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
               401: {'desription': 'Unauthorized'}}
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def home():
    return {"message": "Welcome"}


app.include_router(
    auth.login_router,
    prefix='/auth',
    tags=['User auth section'])

app.include_router(
    users.router_user,
    prefix="/user",
    tags=['User section']
)

app.include_router(
    customers.router_customer,
    prefix="/customer",
    tags=['Customer section']
)

app.include_router(
    products.router_product,
    prefix="/product",
    tags=['Product section'],

)

app.include_router(
    trade.router_trade,
    prefix="/trade",
    tags=['Trade section']
)

app.include_router(
    order.router_order,
    prefix="/orders",
    tags=['Orders section']
    )

app.include_router(
    balance.router_balance,
    prefix="/balance",
    tags=['Balance section']
    )


app.include_router(
    income.router_income,
    prefix="/income",
    tags=['Income section']
    )



app.include_router(
    expence.router_expence,
    prefix="/expence",
    tags=['Expence section']
    )




app.include_router(
    basement.router_basement,
    prefix="/basement",
    tags=['Basement section']
    )