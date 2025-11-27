import React, { useEffect, useState } from "react";
import api from "../utils/api";
import PlayerStats from "./PlayerStats";
import NotScore from "./NotScore";
import AdvPlayerStats from "./AdvPlayerStats";
import SimilarPlayers from "./SimilarPlayers";
import BestGames from "./BestGames";
import PlayerStatsLast3 from "./PlayerStatsLast3";

const PlayerList = () => {
  const [players, setPlayers] = useState([]);
  const [selectedPlayer, setSelectedPlayer] = useState(null);
  const [isListOpen, setIsListOpen] = useState(true);

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
      <button
        type="button"
        onClick={() => setIsListOpen((prev) => !prev)}
        style={{
          display: "block",
          margin: "10px auto",
          fontSize: "20px"
        }}
        aria-expanded={isListOpen}
      >
        {isListOpen ? "Hide player list ▲" : "Show player list ▼"}
      </button>
      {isListOpen && (
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
      )}

      <button
        type="button"
        onClick={() => setIsListOpen((prev) => !prev)}
        style={{
          display: "block",
          margin: "10px auto",
          fontSize: "20px"
        }}
        aria-expanded={isListOpen}
      >
        {isListOpen ? "Hide player list ▲" : "Show player list ▼"}
      </button>

      {selectedPlayer && (
        <>
        <PlayerStats playerId={selectedPlayer.player_id} playerName={selectedPlayer.name} />
        <AdvPlayerStats playerId={selectedPlayer.player_id} playerName={selectedPlayer.name} />
        <SimilarPlayers playerId={selectedPlayer.player_id} playerName={selectedPlayer.name}/>
        <NotScore playerId={selectedPlayer.player_id} playerName={selectedPlayer.name}/>
        <BestGames playerId={selectedPlayer.player_id} playerName={selectedPlayer.name}/>
        <PlayerStatsLast3 playerId={selectedPlayer.player_id} playerName={selectedPlayer.name}/>
        </>
      )}
    </div>
  );
};

export default PlayerList;