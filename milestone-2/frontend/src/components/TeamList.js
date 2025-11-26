import React, { useEffect, useState } from "react";
import api from "../utils/api";
import TeamRecord from "./TeamRecord";
import TeamRoster from "./TeamRoster";

const TeamList = () => {
  const [teams, setTeams] = useState([]);
  const [selectedTeam, setSelectedTeam] = useState(null);

  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const response = await api.get("/teams/");
        setTeams(response.data.data);
        console.log("Fetched teams");
      } catch (error) {
        console.error("Error fetching teams:", error);
      }
    };
    fetchTeams();
  }, []);

  return (
    <div>
      <h2>Teams</h2>
      <div style={{ display: "flex", "flex-wrap": "wrap", gap: "10px", "justify-content": "center" }}>
        {teams.map((team) => (
          <button
            key={team.team_id}
            onClick={() => setSelectedTeam(team)}
          >
            {team.name}
          </button>
        ))}
      </div>

      {selectedTeam && (
        <>
        <TeamRecord teamId={selectedTeam.team_id} teamName={selectedTeam.name} />
        <TeamRoster teamId={selectedTeam.team_id} teamName={selectedTeam.name} />
        </>
      )}
    </div>
  );
};

export default TeamList;