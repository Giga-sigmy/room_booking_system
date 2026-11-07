import type { Room } from "@/types/room";
import RoomCard from "./RoomCard";

type RoomListProps = {
  rooms: Room[];
};

export default function RoomList({ rooms }: RoomListProps) {
  if (rooms.length === 0) {
    return <p className="page-description">No rooms found.</p>;
  }

  return (
    <div className="room-list">
      {rooms.map((room) => (
        <RoomCard key={room.id} room={room} />
      ))}
    </div>
  );
}