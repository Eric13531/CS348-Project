import React, { useEffect, useState } from "react";
import api from "../utils/api";

const BestGames = ({ playerId, playerName }) => {
  const [games, setGames] = useState(null);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const response = await api.get(`/player_best_games/?player_id=${playerId}`);
        setGames(response.data.data);
        console.log("Games retrieved for player id:", playerId)
      } catch (error) {
        console.error("Error fetching player games:", error);
      }
    }
    fetchStats();
  }, [playerId]);

  if (games === null) {
    return <p>Loading stats...</p>;
  }

    return (
    <div style={{ marginTop: "10px", "textAlign": "center" }}>
      <h3>{playerName}'s exceptional games</h3>
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
        {games.length === 0 ? <p>Player has no games significantly above average</p>
          : <>
            <ul style={{ "list-style-type": "none", marginTop: "-10px", paddingLeft: "0px", display: "flex", flexDirection: "column"}}>
              {games.map((game, idx) => (
                    
                <span key={game.game_id}>
                  ({game.date}) {game.home_team_name} -- {game.away_team_name}, {game.points} points
                </span>
              ))}
            </ul>
          </>}
      </div>
    </div>
  );
};

export default BestGames;