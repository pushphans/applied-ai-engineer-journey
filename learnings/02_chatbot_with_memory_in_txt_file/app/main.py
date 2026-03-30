from fastapi import FastAPI
from app.api.router import router
from contextlib import asynccontextmanager
from app.core.connection_pool import checkpointer, connection_pool


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    await connection_pool.open()  # Open the connection pool during startup
    await checkpointer.setup()  # Setup the checkpointer during startup

    yield

    print("Shutting down...")
    await connection_pool.close()  # Close the connection pool during shutdown


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(router=router)
