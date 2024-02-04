from firebase_admin import credentials,auth
import pyrebase
import json
from config.config import get_settings

firebase=pyrebase.initialize_app(
get_settings()["FIREBASE_CONFIG"]
)


def SignUp(email,password):
    try:
        user=auth.create_user(email=email,password=password)
        return {"status":"ok","data":user}
    except auth.EmailAlreadyExistsError:
        return {"status":"error","data":"User already exists"}
     

def Login(email,password):

    try:
        user=firebase.auth().sign_in_with_email_and_password(
            email=email,
            password=password
        )
        token=user["idToken"]

        return {"status":"ok","token":token,"data":user}
    except Exception as e:
        print(e)
        return {"status":"error","data":e}
        

def Verify_Token(jwt):
    try:
        user=auth.verify_id_token(jwt)
        
        return {"status":"ok","data":user}

    except Exception as e:
        print(e)
        return {"status":"error","data":e}
