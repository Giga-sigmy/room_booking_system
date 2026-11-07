from pydantic import BaseModel
from fastapi import APIRouter, Request, HTTPException
from typing import List

router = APIRouter(prefix="/rooms", tags=["rooms"])

class Room(BaseModel):
    floor: int
    id: int
    name: str
    capacity: int

_rooms: dict[int, Room] = {}


@router.post("")
async def create_room(request: Request) -> Room:
    floor = request.query_params.get("floor")
    id_ = request.query_params.get("id")
    name = request.query_params.get("name")
    capacity = request.query_params.get("capacity")
    if floor is None or id_ is None or name is None or capacity is None:
         raise HTTPException(status_code=422, detail="Value incorrect")
    room = Room(
        floor = int(floor),
        id = int(id_),
        name = str(name),
        capacity = int(capacity),
    )
    _rooms[room.id] = room
    return room

@router.get("")

async def get_rooms() -> List[Room]:
    return list(_rooms.values())


@router.get("/{id}")
async def get_room(id: int) -> Room:
    room =  _rooms.get(id)
    if room:
        return room
    else:
        raise HTTPException(status_code=404, detail="Room not found")

@router.post("/{id}")
async def update_room(request: Request, id: int) -> Room:
    room = _rooms.get(id)
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")

    name = request.query_params.get("name")
    capacity = request.query_params.get("capacity")
    if name is not None:
        room.name = name
    if capacity is not None:
        room.capacity = int(capacity)
    return room

@router.delete("/{id}", status_code=204)
async def delete_room(id: int) -> None:
    room = _rooms.get(id)
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    del _rooms[id]





