from fastapi import APIRouter, status, Response, HTTPException
from model.model import Users, Otp, VerifyOtp
from conversion.conversion import convertUser
from password_validator import PasswordValidator
from myconfiq.myconfiq import Blog, Otp_collection
import validators
import random
import smtplib 
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
# from datetime import datetime, timedelta
# expired_limit = 1 

movement = APIRouter()

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "app.lovemeet@gmail.com"
smtp_password = "dwiy ocos hsnp csuh"
SENDER_EMAIL = "app.lovemeet@gmail.com"

def send_mail(receiver_email, subject, message):
     msg = MIMEMultipart()
     msg["From"] = SENDER_EMAIL 
     msg["To"] = receiver_email 
     msg["subject"] = subject 
     msg.attach(MIMEText(message, "plain"))
     try:
          server = smtplib.SMTP(smtp_server, smtp_port)
          server.ehlo()
          server.starttls()
          server.login(smtp_username, smtp_password)
          server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
          server.quit()
          print(" Message has been sent to ur inbox")
     except Exception as e:
          print("Failed to send message, error:", str(e))

def genOtp():
     return random.randint(100000, 900000)

@movement.post("/send-otp")
def send_otp(data: Otp):
     otp = genOtp()
     subject = "Login for OTP verification"
     message = f"Your OTP is: {otp}"
     send_mail(data.email, subject, message)
     print(otp)
     Otp_collection.insert_one({"email": data.email, "otp": otp} )
     return {"Message": "OTP has been sent to your email"}

@movement.post("/verification")
def verified(data: VerifyOtp, response: Response):
   record =  Otp_collection.find_one({"email": data.email, "otp": data.otp})    
   if not record:
        response.status_code = status.HTTP_400_BAD_REQUEST 
        return {"error": "Invalid OTP"}



   Otp_collection.delete_one({"_id": record["_id"]})        
   return {"Message": "OTP has been verified"}              





schema = PasswordValidator()


schema\
.min(8)\
.max(100)\
.has().uppercase()\
.has().lowercase()\
.has().digits()\
.has().no().spaces()\


@movement.get("/welcome")
def welcome():
     return {"Message": "Welcome", "Option": ["Login", "Sign up"]}


@movement.post("/signup", status_code=200)
def routerLog(user: Users, response: Response ):
    user_dict = user.dict()
    if user_dict["firstname"] == "":
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "First name is required"}
    
    if user_dict["lastname"] == "":
          response.status_code = status.HTTP_400_BAD_REQUEST
          return {"error": "Last name is required"}
    if user_dict["age"] == "":
          response.status_code = status.HTTP_400_BAD_REQUEST
          return {"error": "Age is required"}    
     
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
    
    
    res = Blog.insert_one(user_dict)
    result = Blog.find_one({"_id": res.inserted_id})
    return convertUser(result)
    

    
    

    

