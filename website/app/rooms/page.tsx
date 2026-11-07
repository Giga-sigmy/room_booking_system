import RoomList from "@/components/rooms/RoomList";
import { mockRooms } from "@/lib/mock-rooms";

export default function RoomsPage() {
  return (
    <main>
      <div className="page-container">
        <h1 className="page-title">Browse Rooms</h1>

        <p className="page-description">
          Explore available rooms.
        </p>

        <RoomList rooms={mockRooms} />
      </div>
    </main>
  );
}