import React, { useEffect, useState } from "react";
import api from "../utils/api";

const GameStats = ({ gameId }) => {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const response = await api.get(`/game_leaders/?game_id=${gameId}`);
        setStats(response.data.data);
        console.log(response.data.data)
        console.log("Stats retrieved for game id:", gameId)
      } catch (error) {
        console.error("Error fetching game stats:", error);
      }
    }
    fetchStats();
  }, [gameId]);

  if (!stats) return <p>Loading stats...</p>;

  return (
    <div>
      <h3>Stats</h3>
      <div style={{ display: "flex", "flex-wrap": "wrap", gap: "10px", "justify-content": "center" }}>
      <ul style={{ "list-style-type": "none", marginTop: "-10px", paddingLeft: "0px", display: "flex", flexDirection: "column"}}>
        {stats.map((stat, idx) => (
          <span key = {stat.player_id}><b>{stat.player_name}</b>, Minutes: {stat.minutes}, Points: {stat.points}, Assists: {stat.assists}, Threes: {stat.three_p}, Steals: {stat.steals}, Blocks: {stat.blocks}</span>
        ))}
      </ul>
      </div>
    </div>
  );
};

export default GameStats;