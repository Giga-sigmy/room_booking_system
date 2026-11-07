from fastapi import FastAPI
from rooms import router as rooms_router


app = FastAPI()
app.include_router(rooms_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health_check():
    return {"status": "ok"}