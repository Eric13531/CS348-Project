import React, { useEffect, useState } from "react";
import api from "../utils/api";

const NotScore = ({ playerId, playerName }) => {
  const [teams, setTeams] = useState(null);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const response = await api.get(`/player_not_score/?player_id=${playerId}`);
        setTeams(response.data.data);
        console.log("Stats retrieved for player id:", playerId)
      } catch (error) {
        console.error("Error fetching player stats:", error);
      }
    }
    fetchStats();
  }, [playerId]);

  if (teams === null) {
    return <p>Loading stats...</p>;
  }

    return (
    <div style={{ marginTop: "10px", "textAlign": "center" }}>
      <h3>Teams that {playerName} hasn't scored against</h3>
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
        {teams.length === 0 ? <p>Player has scored against all teams they played against</p>
          : <>
            {teams.map((team, idx) => (
              <span key={team.team_id}>
                {team.team_name}{idx < teams.length - 1 ? "," : ""}
              </span>
            ))}
          </>}
      </div>
    </div>
  );
};

export default NotScore;