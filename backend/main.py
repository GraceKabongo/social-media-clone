from fastapi import FastAPI
from routes import user

app = FastAPI()

app.include_router(user.router, tags=["users"])

@app.get("/")
def read_root():
    return {"Hello": "World"}