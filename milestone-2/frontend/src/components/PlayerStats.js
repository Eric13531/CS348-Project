import React, { useEffect, useState } from "react";
import api from "../utils/api";

const PlayerStats = ({ playerId }) => {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const response = await api.get(`/player_averages/?player_id=${playerId}`);
        setStats(response.data.data[0]);
        console.log("Stats retrieved for player id:", playerId)
      } catch (error) {
        console.error("Error fetching player stats:", error);
      }
    }
    fetchStats();
  }, [playerId]);

  if (!stats) return <p>Loading stats...</p>;

  return (
    <div style={{ display: "flex", "flex-wrap": "wrap", gap: "10px", "justify-content": "center" }}>
      <h3>{stats.name}'s Averages:</h3>
      <ul style={{ "list-style-type": "none", marginTop: "20px", display: "flex"}}>
        <li style = {{margin: "3px", marginRight: "10px"}}>Points: {stats?.avg_points?.toFixed(1) ?? "N/A"}</li>
        <li style = {{margin: "3px", marginRight: "10px"}}>Assists: {stats?.avg_assists?.toFixed(1) ?? "N/A"}</li>
        <li style = {{margin: "3px", marginRight: "10px"}}>Steals: {stats?.avg_steals?.toFixed(1) ?? "N/A"}</li>
        <li style = {{margin: "3px", marginRight: "10px"}}>Blocks: {stats?.avg_blocks?.toFixed(1) ?? "N/A"}</li>
      </ul>
    </div>
  );
};

export default PlayerStats;