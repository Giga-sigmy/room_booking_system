from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter(prefix="/rooms", tags=["rooms"])

class Room(BaseModel):
    floor: int
    id: int
    name: str
    capacity: int
