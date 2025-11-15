import React, { useEffect, useState } from "react";
import api from "../utils/api";

const TeamRoster = ({ teamId, teamName }) => {
  const [roster, setRoster] = useState(null);

  useEffect(() => {
    const fetchRoster = async () => {
      try {
        const response = await api.get(`/team_roster/?team_id=${teamId}`);
        setRoster(response.data.data);
        console.log("Stats retrieved for team id:", teamId)
      } catch (error) {
        console.error("Error fetching team:", error);
      }
    }
    fetchRoster();
  }, [teamId]);

  if (!roster) return <p>Loading roster...</p>;

  if (roster) {
    console.log("roster", roster)
  }

  return (
    <div style={{ display: "flex", "flex-wrap": "wrap", gap: "10px", "justify-content": "center", flexDirection: "column"}}>
      <h3>{teamName}'s Roster:</h3>
      <ul style={{ "list-style-type": "none", marginTop: "-10px", display: "flex", flexDirection: "column"}}>
        {roster.map(player => (
          <li key = {player.player_id}>{player.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default TeamRoster;