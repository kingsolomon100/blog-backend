from fastapi import FastAPI
from route.route import router
from login.login import movement
app = FastAPI()

app.include_router(router)
app.include_router(movement) 