
# class Item(BaseModel):
#     email: str 
#     password: str
#     pin: int| str



# @app.get("/bot")
# def read_root():
#     return {"data": "james is a pastor"}

# allData = [{
#     "name": "james",
#     "age": 50,
#     "city": "london"
# }]

# @app.get("/get-all-data")

# def getAllData():
#     return {"data": allData}

# @app.get("/")
# def read_root():
#     return {"data": "welcome to my api"}

# myData = [{
#     "name": "godson",
#     "age": 24,
#     "city": "lagos",
#     "course": "frontend"
# }]
# @app.get("/get-name")
# def getName():
#     return ({"name": myData["name"]})

# @app.get("/get-age")
# def getAge():
#     return ({"age": myData[0]["age"]})

# @app.get("/get-city")
# def getCity():
#     return ({"city": myData[0]["city"]})

# @app.get("/get-course")
# def fetchCourse():
#     for i in myData:
#      return ({"course": myData[i]["course"]})
#     print(myData)



# from fastapi import FastAPI, HTTPException 
# from pydantic import BaseModel 


# app = FastAPI()
 
# class Item(BaseModel):
#     pin: str

# class User(BaseModel):
#     new_pin: str 

# allData = []

# def validation(pin: str):
#     if not pin.isdigit():
#         raise HTTPException(status_code=400, detail="It must be numbered")

#     if len(pin) != 10:
#          raise HTTPException(status_code=400, detail="It must be exactly 10 digit")
    
#     if pin[0] =="0":
#          raise HTTPException(status_code=400, detail="It must not start with zero")
    
# @app.post("/create-user")
# def poster(data: Item):
#     validation(data.pin)
#     allData.append(data)
#     return {"Message": "User pin is accessibly correct"}

# @app.put("/users/{user_id}")
# def update(user_id: int, data: User):
#     if user_id < 0 or user_id >= len(allData):
#         raise HTTPException(status_code=400, detail="userid not found")
#     validation(data.new_pin)

#     allData[user_id].pin = data.new_pin 
#     return {"Message": "user pin has been updated"}
    
 



        





# from fastapi import FastAPI
# from pydantic import BaseModel
# app = FastAPI()

# class Item(BaseModel):
#     email: str 
#     password: str|int
#     name: str 
#     courses: list[str] 
#     state: str 
#     plans: dict = {}

# class Aus(BaseModel):
#      email: str 
#      password: str | int     

# database = []

# @app.post("/create-account")

# def createAccount(data: Item):
#         if data.name == "":
#             return {"message": "Failed to create account", "error": "name is required"  }
        
#         elif data.email == "":
#             return {"message": "Failed to create account", "error": "Email is required"  }
#         elif data.state == "":
#             return {"message": "Failed to create account", "error": "state is required"  }
#         elif data.courses == 0:
#             return {"message": "Failed to create account", "error": "courses is required"  }
#         else:
#              return{"data": "Account successfully created"}
        

    



# @app.patch("/update-account")
# def updateAccount(data: Item):
#      database.append(data)
#      return {"data": "account successfully"}


# @app.post("/login-account")
# def login(data: Aus):
#     #  database.append(data)
#     return {"data": "login successfully"}
        
        
# @app.get("/fetch-account")
# def fetchAccount():
#     return{"account": database}
          
     
# @app.get("/fetch-user/{userID}")
# def fetchAccount(userId: str):
#     return{"account": userId}    






# from fastapi import FastAPI, HTTPException 
# from pydantic import BaseModel

# app = FastAPI()



# class ProductModel(BaseModel):
#     id: int | None = None
#     name: str
#     price: str| int
#     colour: str
    


# products=[]

# @app.post("/add-product")
# def addProduct(product: ProductModel):
#      product.id= len(products) + 1
#      products.append(product)
#      return {"Message": f"{product.name} is added successfully", "Data": product}
   
   
# @app.get("/products")
# def get_all_products():
#      return{"total": len(products),"data": products}

# @app.get("/product/{productId}")
# def get_product(productId: int):
#      for x in products:
#          if x["Id"] == productId:
#                 return{"account": x}            
#      else:
#           raise HTTPException(status_code=404, detail="product not found")          
               

     
          
         
     
# @app.delete("/products/{product_id}") 
# def delete_product_by_id(product_id: int):
#      for i, item in enumerate(products):
#           if item["Id"] == int(product_id):
#                deleted = products.pop(i)     
#                return{"message": "product deleted successfully","deleted_product": deleted}


# from fastapi import FastAPI, HTTPException 
# from pydantic import BaseModel

# app = FastAPI()



# class User(BaseModel):
#     username: str
#     country: str
#     pin: str | int

# users = []    



# @app.post("/create-username")
# def postUser(user: User):
#     data ={
#         "id": len(users) + 1,
#         "username": user.username,
#         "country": user.country,
#         "pin": user.pin
#     }
#     users.append(data)
#     return {"Message": "User's name added successfully", "data": user }

# @app.put("/users/{username}/update_pin")
# def patchPin(username: str, new_pin: int ):
#     for user in users:
#         if user["username"] == username:
#             user['pin'] = new_pin
#             return {"Message": "User pin has been updated", "user": user }
#     else:
#         raise HTTPException(status_code=400, detail="Error Detented!") 
           
     
        
# @app.put("/users/{old_username}/update_username")
# def patchName(old_username: str, new_username: str):
#     for user in users:
#         if user["username"] == old_username:
#             user["username"] = new_username 
#             return {"Message": "User's Name has been updated", "User": user}        
            
#     else:
#         raise HTTPException(status_code=400, detail="Error Detented!")
    
# @app.delete("/user-delete/{user_delete}")
# def userDelete(user_delete: str):
#     for i, user in enumerate(users):
#         if user["username"] == (user_delete):     
#           deleted =  users.pop(i)
#           return {"Message": "User's name has been deleted", "user": deleted }
#     else:
#         raise HTTPException(status_code=404, detail="error found")    
        
# @app.get("/users/{username}")
# def getUser(username: str):
#     for user in users:
#         if user["username"] == (username):
#             return {"user": user}
#     else:
#          raise HTTPException(status_code=404, detail="error found")    
        

        


# @app.get("/data")
# def get_all_data():
#      return{"total": len(users),"data": users}

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel 

# class Worker(BaseModel):
#     usename: str 
#     country: str
#     pin:     str 


# app = FastAPI()

# users = []


# @app.post("/create_post" )
# def createPost(user: Worker):
#     data = {
#         "usename": user.usename,
#         "country": user.country,
#         "pin":    user.pin 
#     }
#     users.append(data)
#     return {"message": "user name added successfully", "User": user}

# @app.get("/get_info")
# def getInfo():
#     return {"Total number of User": len(users), "data": users}

# @app.put("/users/{user_name}/update_pin")
# def updatePin(user_name: str, new_pin: int):
#     for user in users:
#         if user["username"] == user_name:
#             user['pin'] = new_pin 
#             return {"message": "user name has been updated"}


# from fastapi import FastAPI, HTTPException 
# from pydantic import BaseModel 
# app = FastAPI()


# class Worker(BaseModel):
#     username: str 
#     pin:      str|int 
#     state:    str 
#     institution: str 
#     password:    str|int 


# users = []


# @app.post("/create_worker")
# def workInput(info: Worker):
#     data = {
#         "username": info.username,
#         "pin": info.pin,
#         "state": info.state,
#         "institution": info.institution,
#         "password": info.password
#     }
#     users.append(data)
#     return {"Message": "User's detail is added successfully", "data": info }

# @app.get("/get_info")
# def getInfo():
#     return {"Total of workers": len(users), "Data": users }



# @app.put("/user/{password}/update_state")
# def updateState(password: int, new_state: str):
#     for user in users:
#         if user["password"] == password:
#             user["state"] = new_state 
#             return {"Message": f"User's state has been change to {new_state} ", "Data": user}
        
#     raise HTTPException(status_code=400, detail="user's password not found, try again")

# @app.put("/info/{username}/update_sch")
# def updateSch(username: str, new_sch: str):
#     for user in users:
#         if user["username"] == username:
#             user["institution"] = new_sch 
#             return {"Message": f"School updated 'congratulation' to {username}", "Data": user}
        
#     raise HTTPException(status_code=400, detail="user's password not found, try again")

# @app.delete("/user/{username}")
# def deleteUserName(username: str):
#     for i, user in enumerate(users):
#         if user["username"] == username:
#             deleted = users.pop(i)
#             return{"message": f"name successfully deleted", "Deleted from the profile": deleted}

#     raise HTTPException(status_code=400, detail="user's password not found, try again")




# @app.get("/get/{username}")
# def get_it(username: str):
#     for user in users:
#         if user["username"] == username:
#             return {"User": user}
#     raise HTTPException(status_code=400, detail="user's password not found, try again")
    

# @app.delete("/momo/{username}")
# def momo(username: str):
#     for i, user in enumerate(users):
#         if user["username"] == username:
#             deleted = users.pop(i)
#             return {"Message": f"{username} has been deleted from the list", "Deleted": deleted}
#     raise HTTPException(status_code=400, detail="user's password not found, try again")

# from pymongo import MongoClient
# uri = "mongodb://localhost:27017"
# client = MongoClient(uri)

# try:
#     print("database connected")
#     client.close()

# except Exception as e:
#     raise Exception("Unable to find the document due to the following error: ", e)

# 

from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel 

app = FastAPI()

class Product(BaseModel):
    id: int| None = None
    name: str 
    price: int 
    colour: str 

class Client(BaseModel):
    client_id: int| None = None 
    client_name: str 
    products: list[Product] = []


clients = []


@app.post("/create-client")
def poster(client: Client):
    client.client_id = len(clients) + 1 
    clients.append(client) 
    return {"Message": "Client name added successfully", "Name": client}


@app.post("/add-product/{client_id}/products") 
def addProduct(client_id: int, product: Product):
    for client in clients:
        if client.client_id == client_id:
            product.id = len(client.products) + 1 
            client.products.append(product)
            return {"Message": f"{client.client_name} is added successfully", "Product": product}
        
    raise HTTPException(status_code=400, detail="clientId is not found")  
 
@app.put("/update-client/{client_id}/product_id/{product_id}")
def updateProduct(client_id: int, product_id: int, data: Product):
    for client in clients:
        if client.client_id == client_id:
            for product in client.products:
                if product.id == product_id:
                    product.name = data.name 
                    product.price = data.price 
                    product.colour = data.colour 
                    return {"Message": "products is updated successfully", "Updated products": product}

    raise HTTPException(status_code=400, detail="clientId is not found")  

@app.patch("/clients/{client_id}/update-name")
def updateName(client_id: int, new_name: str):
    for client in clients:
        if client.client_id == client_id:
            client.client_name = new_name
            return {"Message": "Client name has been updated", "clientid": client_id, "New name": new_name  }
    raise HTTPException(status_code=400, detail="clientId is not found")  
    

@app.get("/clients/{client_id}/products")
def gett(client_id: int):
    for client in clients:
        if client.client_id == client_id:
            return {"Message": client.client_name, "Total of products": len(client.products), "Data": client.products}    
    raise HTTPException(status_code=400, detail="clientId is not found")  
    


             