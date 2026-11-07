"use client"

import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function Home() {
  const ip: string = process.env.NEXT_PUBLIC_API_IP ?? "";
  const router = useRouter();

  const handleFloorButtonClick = () => {
    router.push("/floor");
  };

  const handleRoomsButtonClick = () => {
    router.push("/rooms");
  };

  const pingApi = () => {
    if (!ip) return;

    fetch(`${ip}/health`)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data: { status: string }) => {
        const result = { status: data.status };
        if (result.status !== "ok") {
          throw new Error(`HTTP error! status: ${result.status}`);
        }
      })
      .catch((error) => console.error("Error:", error));
  };

  useEffect(() => {
    pingApi();
  }, []);

  return (
    <main>
      <h1>
        Room booking system is application for booking rooms.
        You can book room from rooms list or easly pick from the floor layout.
      </h1>
      <div className="content-row">
        <div className="row">
          <button type="button" onClick={handleRoomsButtonClick}>
            Click to see rooms list
          </button>
          <button type="button" onClick={handleFloorButtonClick}>
            Click to see floor layout
          </button>
        </div>
      </div>
    </main>
  );
}
