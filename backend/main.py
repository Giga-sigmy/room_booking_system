from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from rooms import router as rooms_router
from connectors.database import get_db

app = FastAPI()

app.include_router(rooms_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/health/db")
def database_health(db = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"database": "connected"}