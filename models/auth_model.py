from pydantic import BaseModel

class SignUpSchema(BaseModel):
    email: str
    password: str
    username: str

    class Config:
        json_schema_extra={
            "example":{
                "username":"baka",
                "email":"test@gmail.com",
                "password":"pass123"
            }
        }


class LoginSchema(BaseModel):
    email: str
    password: str

    class Config:
        json_schema_extra={
            "example":{
                "email":"test@gmail.com",
                "password":"pass123"
            }
        }
