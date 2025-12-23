from fastapi import APIRouter, status, Response
from model.model import Users
from conversion.conversion import convertUser 
from password_validator import PasswordValidator
from myconfiq.myconfiq import Userlogin
import validators

signin = APIRouter()
 
schema = PasswordValidator()


schema\
.min(8)\
.max(100)\
.has().uppercase()\
.has().lowercase()\
.has().digits()\
.has().no().spaces()\



@signin.post("/sign-in", status_code=200)
def signInLog(user: Users, response: Response ):
    user_dict = user.dict()
    if user_dict["username"] == "":
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Username is required"}
    
    if user_dict["password"] == "":
         response.status_code = status.HTTP_400_BAD_REQUEST
         return {"error": "Password is required"}
    
    if not schema.validate(user_dict["password"]):
         response.status_code = status.HTTP_400_BAD_REQUEST
         return {"error": "Password is not strong enough"}
    
    if user_dict["email"] == "":
          response.status_code = status.HTTP_400_BAD_REQUEST
          return {"error": "Email is required"}
    
    if not validators.email(user_dict["email"]):
          response.status_code = status.HTTP_400_BAD_REQUEST
          return {"error": "Email is not a email address"}
    
    res = Userlogin.insert_one(user_dict)
    result = Userlogin.find_one({"_id": res.inserted_id})
    return convertUser(result)
    

    
    

    

