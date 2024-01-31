from fastapi import APIRouter
import firebase_admin
from firebase_admin import credentials

from models import auth_model
import json
from helper import FirebaseAuth
from config import database
from fastapi.requests import Request

if not firebase_admin._apps:
    cred = credentials.Certificate(r"config/hpmp-9a745-firebase-adminsdk-3f2g3-678ae3dfa0.json")
    firebase_admin.initialize_app(cred)



auth_router=APIRouter()

@auth_router.post("/signup")
async def create_account(user_data: auth_model.SignUpSchema):

    if database.users.find_one({"username":user_data.username}) is None:
        
            email=user_data.email
            password=user_data.password
            response=FirebaseAuth.SignUp(email,password)
            print(response["data"].uid)
            
            if response["status"]!="error":
                 database.users.insert_one({"_id":response["data"].uid,"recently_played":[],"playlists":[],"username":user_data.username})
            return response
    else:
         return {"status":"error","data":"Username already exists"}
    
@auth_router.post("/login")
async def login_user(user_data: auth_model.LoginSchema):
        email=user_data.email
        password=user_data.password

        response=FirebaseAuth.Login(email,password)

        if response["status"]=="ok":
             user=database.users.find_one({"_id":response["data"]["localId"]})
             
             return {"status":"ok","token":response["token"],"user":user}
        else:
             return response

@auth_router.get("/validate")
async def validate(request:Request):
    return {"status":"ok"} #remove this after dev
    headers=request.headers
    jwt= headers.get("authorization")
    response=FirebaseAuth.Verify_Token(jwt)
    
    