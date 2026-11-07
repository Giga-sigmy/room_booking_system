from pydantic import BaseModel
from fastapi import APIRouter, Request
from typing import List

router = APIRouter(prefix="/rooms", tags=["rooms"])

class Room(BaseModel):
    floor: int
    id: int
    name: str
    capacity: int
    class Config:
        orm_mode = True
        schema_extra = {}

@router.post("/rooms")
async def create_room(request: Request) -> Room:
    room = Room(
        floor=request.query_params.get("floor"),
        id=request.query_params.get("id"),
        name=request.query_params.get("name"),
        capacity=request.query_params.get("capacity"),
    )
    return room

@router.get("/rooms")

async def get_rooms() -> List[Room]:
    return [room.json() for room in Room.objects.all()]

@router.get("/rooms/{id}")
async def get_room(id: int) -> Room:
    return Room.objects.get(id=id)

@router.post("/rooms/{id}")
async def update_room(request: Request, id: int) -> Room:
    room = Room.objects.get(id=id)
    room.name = request.query_params.get("name")
    room.capacity = request.query_params.get("capacity")
    room.save()
    return room.json()





