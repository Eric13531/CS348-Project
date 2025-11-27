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
    <div>
      <h3>{teamName}'s Roster:</h3>
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
        {roster.map((player, idx) => (
          <span key = {player.player_id}>{player.name}{idx < roster.length - 1 ? "," : ""}</span>
        ))}
      </div>
    </div>
  );
};

export default TeamRoster;
