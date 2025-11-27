import React, { useEffect, useState } from "react";
import api from "../utils/api";

const AdvPlayerStats = ({ playerId }) => {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const response = await api.get(`/player_advanced/?player_id=${playerId}`);
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
    <div style={{ marginTop: "10px", "textAlign": "center" }}>
      <h3>{stats.name}'s Totals:</h3>
      <ul style={{ "list-style-type": "none", margin: 0, padding: 0, display: "flex", justifyContent: "center"}}>
        <li style = {{margin: "3px", marginRight: "10px"}}>Games Played: {stats?.games_played ?? "N/A"}</li>
        <li style = {{margin: "3px", marginRight: "10px"}}>Total Minutes: {stats?.total_minutes ?? "N/A"}</li>
        <li style = {{margin: "3px", marginRight: "10px"}}>Total Points: {stats?.total_points ?? "N/A"}</li>
        <li style = {{margin: "3px", marginRight: "10px"}}>Total Assists: {stats?.total_assists ?? "N/A"}</li>
        <li style = {{margin: "3px", marginRight: "10px"}}>Total Steals: {stats?.total_steals ?? "N/A"}</li>
        <li style = {{margin: "3px", marginRight: "10px"}}>Total Blocks: {stats?.total_blocks ?? "N/A"}</li>
      </ul>
    </div>
  );
};

export default AdvPlayerStats;