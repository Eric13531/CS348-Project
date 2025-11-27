import React, { useEffect, useState } from "react";
import api from "../utils/api";

const PlayerStatsLast3 = ({ playerId }) => {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const response = await api.get(`/player_stats_last_3/?player_id=${playerId}`);
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
      <h3>{stats.player_name}'s Averages Over Last 3 Games:</h3>
      <ul style={{ "list-style-type": "none", margin: 0, padding: 0, display: "flex", justifyContent: "center"}}>
        <li style = {{margin: "3px", marginRight: "10px"}}>Points: {stats?.rolling_pts_last_3?.toFixed(1) ?? "N/A"}</li>
        <li style = {{margin: "3px", marginRight: "10px"}}>Assists: {stats?.rolling_asts_last_3?.toFixed(1) ?? "N/A"}</li>
        <li style = {{margin: "3px", marginRight: "10px"}}>Steals: {stats?.rolling_stls_last_3?.toFixed(1) ?? "N/A"}</li>
        <li style = {{margin: "3px", marginRight: "10px"}}>Blocks: {stats?.rolling_blks_last_3?.toFixed(1) ?? "N/A"}</li>
      </ul>
    </div>
  );
};

export default PlayerStatsLast3;