from uvicorn import run

from fastapi import FastAPI

from core.utils.case import to_snake


app = FastAPI()


@app.get("/")
def root():
    return {
        "ok": True,
    }


if __name__ == "__main__":
    run("main:app", reload=True)
