def convertblog(project) -> dict:
    return {
        "_id": str(project["_id"]),
        "categories": project["categories"],
        "category": project["category"],
        "title": project["title"],
        "subtitle": project["subtitle"],
        "content": project["content"],
        "image": project["image"],
        "timedate": project["timedate"]
    } 

def convertblogs(projects) -> list:
    return [convertblog(project) for project in projects ]


def convertUser(user) -> dict:
    return {
        "_id": str(user["_id"]),
        "firstname": user["firstname"],
        "lastname": user["lastname"],
        "age": user["age"],
        "password": user["password"],
        "email": user["email"]

    }



    