from fastapi import FastAPI

from .routes import students

app = FastAPI()

app.include_router(students.router)


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}