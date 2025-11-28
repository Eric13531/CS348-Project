import React, { useEffect, useState } from "react";
import api from "../utils/api";
import TeamRecord from "./TeamRecord";
import TeamRoster from "./TeamRoster";
import TeamMatchups from "./TeamMatchups";

const TeamList = () => {
  const [teams, setTeams] = useState([]);
  const [selectedTeam, setSelectedTeam] = useState(null);
  const [isListOpen, setIsListOpen] = useState(true);
  const [team1Id, setTeam1Id] = useState(null);
  const [team2Id, setTeam2Id] = useState(null);
  const [team1Name, setTeam1Name] = useState(null);
  const [team2Name, setTeam2Name] = useState(null);

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
      <button
        type="button"
        onClick={() => setIsListOpen((prev) => !prev)}
        
        style={{
          display: "block",
          margin: "10px auto",
          fontSize: "20px"
        }}
        aria-expanded={isListOpen}
      >
        {isListOpen ? "Hide team list ▲" : "Show team list ▼"}
      </button>
      {isListOpen && (
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
      )}
      <button
        type="button"
        onClick={() => setIsListOpen((prev) => !prev)}
        
        style={{
          display: "block",
          margin: "10px auto",
          fontSize: "20px"
        }}
        aria-expanded={isListOpen}
      >
        {isListOpen ? "Hide team list ▲" : "Show team list ▼"}
      </button>

      {selectedTeam && (
        <>
        <TeamRecord teamId={selectedTeam.team_id} teamName={selectedTeam.name} />
        <TeamRoster teamId={selectedTeam.team_id} teamName={selectedTeam.name} />
        </>
      )}
      
      <h3>Teams Matchups</h3>

      <div
        style={{
          display: "flex",
          gap: "12px",
          justifyContent: "center",
          marginBottom: "12px",
          flexWrap: "wrap",
        }}
      >
        <select
          value={team1Id}
          onChange={(e) => {setTeam1Id(e.target.value)}}
        >
          <option value="">Select Team 1</option>
          {teams.map((team) => (
            <option key={team.team_id} value={team.team_id}>
              {team.name}
            </option>
          ))}
        </select>

        <select
          value={team2Id}
          onChange={(e) => setTeam2Id(e.target.value)}
        >
          <option value="">Select Team 2</option>
          {teams.map((team) => (
            <option key={team.team_id} value={team.team_id}>
              {team.name}
            </option>
          ))}
        </select>
      </div>

      {team1Id && team2Id && team1Id !== team2Id && (
        <TeamMatchups teamId1={team1Id} teamName1={team1Name} teamId2={team2Id} teamName2={team2Name}/>
      )}
    </div>
  );
};

export default TeamList;