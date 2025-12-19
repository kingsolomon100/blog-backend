from fastapi import APIRouter, status, Response 
from bson.objectid import ObjectId
from myconfiq.myconfiq import Blog
from model.model import Blogmodel
from conversion.conversion import convertblog, convertblogs 
# import random 
 
router = APIRouter()

@router.post("/post-blog", status_code=200)
async def postman(blog: Blogmodel, response: Response ):
     
    blog_dict = blog.dict()
    if not blog_dict["categories"]:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Categories is required"}
    
    if not blog_dict["category"]:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Category is required"}
    
    if not blog_dict["title"]:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "title is required"}
    
    if not blog_dict["subtitle"]:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "subtitle is required"}
    
    if not blog_dict["image"]:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "image is required"}
    
    if not blog_dict["content"]:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "content is required"} 
    
    res = Blog.insert_one(blog_dict)
    result = Blog.find_one({"_id": res.inserted_id})
    return convertblog(result)
    


@router.get("/get-all-blog")
async def getAll():
    res = list(Blog.find())
    total_blog = len(res)
    return {"Total-blog": total_blog, "Blog list": convertblogs(res)}

@router.get("/get-single-blog/{id}")
def getSingleBlog(id: str, response: Response):
    if not id:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "ID is required"}
    res = Blog.find_one({"_id": ObjectId(id)})
    if not res:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"Message": "ID is not found"}
    else:
       return convertblog(res)

@router.delete("/delete-blog/{id}")
async def deleteBlog(id: str, response: Response):
    res = Blog.find_one({"_id": ObjectId(id)})
    if not res:
        response.status_code = status.HTTP_400_BAD_REQUEST 
        return {"error": "Blog ID is not found"}
    else:
        Blog.delete_one({"_id": ObjectId(id)})
        return {"BlogID has been deleted successfully"}       

@router.put("/update-blog/{id}/{categories}")
def updateBlog(id: str, categories: str, response: Response):  
    if id == None:
         response.status_code = status.HTTP_400_BAD_REQUEST 
         return {"error": "Id is required"}
    
    res = Blog.find_one({"_id": ObjectId(id)})
    if not res:
         response.status_code = status.HTTP_400_BAD_REQUEST
         return {"error": "id is not found"}
    else:
        Blog.update_one({"_id": ObjectId(id)}, {"$set": {"categories": categories}})
        return {"Categories is updated successfully"} 
    

         






    

