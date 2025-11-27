import React, { useEffect, useState } from "react";
import api from "../utils/api";

const SimilarPlayers = ({ playerId, playerName }) => {
  const [similarPlayers, setSimilarPlayers] = useState(null);

  useEffect(() => {
    const fetchRoster = async () => {
      try {
        const response = await api.get(`/similar_players/?player_id=${playerId}`);
        setSimilarPlayers(response.data.data);
        console.log(response.data.data)
        console.log("Similar Players retrieved:", playerId)
      } catch (error) {
        console.error("Error fetching similar players:", error);
      }
    }
    fetchRoster();
  }, [playerId]);

  if (!similarPlayers) return <p>Loading similar player_averages...</p>;

  if (similarPlayers) {
    console.log("roster", similarPlayers)
  }
  
  return (
    <div>
      <h3>{playerName}'s Most Similar Players:</h3>
      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
          gap: "6px",
          marginTop: "10px",
          paddingLeft: "50px",
          paddingRight: "50px",
          justifyContent: "center",
          textAlign: "center"
        }}
      >
        {similarPlayers.map((player, idx) => (
          <span key = {player.player_id}>{player.name}{idx < similarPlayers.length - 1 ? "," : ""}</span>
        ))}
      </div>
    </div>
  );
};

export default SimilarPlayers;
