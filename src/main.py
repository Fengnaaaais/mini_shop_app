from uvicorn import run

from fastapi import FastAPI

from core.utils.case import to_snake
from api import router as api_router


app = FastAPI()


app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    run("main:app", reload=True)
