from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from app.api.router import router

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


app.include_router(router)
