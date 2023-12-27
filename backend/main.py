from fastapi import FastAPI
# from decouple import config

# API_USERNAME = config('MONGODB_URL')

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}