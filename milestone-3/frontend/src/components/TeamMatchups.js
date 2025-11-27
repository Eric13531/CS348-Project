import React, { useEffect, useState } from "react";
import api from "../utils/api";

const TeamMatchups = ({ teamId1, teamName1, teamId2, teamName2 }) => {
  const [matchups, setMatchups] = useState(null);

  useEffect(() => {
    const fetchMatchups = async () => {
      try {
        const response = await api.get(`/team_matchups/?team_id1=${teamId1}&team_id2=${teamId2}`);
        setMatchups(response.data.data);
        console.log("Matchups retrieved for team id:", teamId1, teamId2)
      } catch (error) {
        console.error("Error fetching Matchups:", error);
      }
    }
    fetchMatchups();
  }, [teamId1, teamId2], );

  if (!matchups) return <p>Loading Matchups...</p>;

  if (matchups) {
    console.log(matchups)
  }

  return (
    <div style={{ marginTop: "12px" }}>
          <h2>
            {matchups[0]['home_team']} vs {matchups[0]['away_team']}
          </h2>
          <ul style={{ listStyleType: "none", padding: 0 }}>
            {matchups.map((game) => (
              <li key={game.game_id} style={{ marginBottom: "4px" }}>
                {game.date} -- {game.away_team} @ {game.home_team} ({game.away_score} -- {game.home_score})
              </li>
            ))}
          </ul>
        </div>
  );
};

export default TeamMatchups;
