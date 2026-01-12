from pydantic import BaseModel 
from datetime import datetime

class Blogmodel(BaseModel):
    categories: str = None
    category: str = None 
    title: str = None
    subtitle: str = None
    image: str = None
    content: str = None
    timedate: int = datetime.now()


class Users(BaseModel):
    firstname: str = None 
    lastname: str = None
    age: str = None
    password: str = None 
    email: str = None

class Otp(BaseModel):
    email: str

class VerifyOtp(BaseModel):
    email: str 
    otp: int  


        



        
    
 