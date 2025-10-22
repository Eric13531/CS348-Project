import React, { useEffect, useState } from "react";
import api from "../utils/api";
import PlayerStats from "./PlayerStats";

const PlayerList = () => {
  const [players, setPlayers] = useState([]);
  const [selectedPlayer, setSelectedPlayer] = useState(null);

  useEffect(() => {
    const fetchPlayers = async () => {
      try {
        const response = await api.get("/players/");
        setPlayers(response.data.data);
        console.log("Fetched players");
      } catch (error) {
        console.error("Error fetching players:", error);
      }
    };
    fetchPlayers();
  }, []);

  return (
    <div>
      <h2>Players</h2>
      <div style={{ display: "flex", "flex-wrap": "wrap", gap: "10px", "justify-content": "center" }}>
        {players.map((player) => (
          <button
            key={player.player_id}
            onClick={() => setSelectedPlayer(player)}
          >
            {player.name}
          </button>
        ))}
      </div>

      {selectedPlayer && (
        <PlayerStats playerId={selectedPlayer.player_id} playerName={selectedPlayer.name} />
      )}
    </div>
  );
};

export default PlayerList;