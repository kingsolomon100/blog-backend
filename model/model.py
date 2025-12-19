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
    
 