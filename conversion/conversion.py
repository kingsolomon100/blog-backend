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


def convertUser(user):
    return {
        "_id": str(user["_id"]),
        "username": user["username"],
        "password": user["password"],
        "email": user["email"]

    }

    