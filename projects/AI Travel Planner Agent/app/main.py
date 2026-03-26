from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "ok"}


app.include_router()