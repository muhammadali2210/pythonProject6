from fastapi import FastAPI


users = FastAPI()

@users.get('/')
def index():
    return {"SALOM MUHAMMADALI_ADXAMOVICH"}