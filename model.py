from pydantic import BaseModel, Field, EmailStr

class UserLogintSchema(BaseModel):
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo" : {
                'email' : 'a@mail.ru',
                'password' : '123' 
            }
        }