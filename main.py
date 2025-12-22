from fastapi import FastAPI;
from route.route import router;
from login.login import signin;
app = FastAPI()

app.include_router(router)
app.including_router(signin)