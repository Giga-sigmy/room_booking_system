import type { Room } from "@/types/room";

type RoomCardProps = {
  room: Room;
};

export default function RoomCard({ room }: RoomCardProps) {
  return (
    <article className="card">
      <h2 className="card-title">Room {room.name}</h2>

      <div className="room-details">
        <p>Floor: {room.floor}</p>
        <p>Capacity: {room.capacity} people</p>
      </div>
    </article>
  );
}