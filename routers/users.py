
from fastapi import APIRouter
from fastapi import APIRouter

from fastapi.responses import JSONResponse
from pydantic import BaseModel

from utils.jwt_manager import generate_token


from schemas.user import User


user_router=APIRouter()









@user_router.post("/login",tags=["Login"],status_code=200)

def login(user:User) :
    if user.email == "admin@example.com" and user.password == "12":
        token:str=generate_token(user.dict())
    
        return JSONResponse(status_code=200,content=token)
    else:
        return JSONResponse(status_code=401,content={"message":"Usuario o contraseña incorrect"} )
    

