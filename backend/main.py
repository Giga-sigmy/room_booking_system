from fastapi import FastAPI
from rooms import router as rooms_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rooms_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health_check():
    return {"status": "ok"}