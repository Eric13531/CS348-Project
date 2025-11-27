import React, { useEffect, useState } from "react";
import api from "../utils/api";

const TeamRecord = ({ teamId, teamName }) => {
  const [record, setRecord] = useState(null);

  useEffect(() => {
    const fetchRecord = async () => {
      try {
        const response = await api.get(`/team_record/?team_id=${teamId}`);
        setRecord(response.data.data[0]);
        console.log("Stats retrieved for team id:", teamId)
      } catch (error) {
        console.error("Error fetching team:", error);
      }
    }
    fetchRecord();
  }, [teamId]);

  if (!record) return <p>Loading record...</p>;

  if (record) {
    console.log(record)
  }

  return (
    <div style={{ display: "flex", "flex-wrap": "wrap", gap: "10px", "justify-content": "center", marginTop: "10px" }}>
      <h3>{record.name}'s Record 2024-25:</h3>
      <ul style={{ "list-style-type": "none", marginTop: "20px", display: "flex"}}>
        <li style = {{margin: "3px", marginRight: "10px"}}>Wins: {record?.wins ?? "N/A"}</li>
        <li style = {{margin: "3px", marginRight: "10px"}}>Losses: {record?.losses ?? "N/A"}</li>
      </ul>
    </div>
  );
};

export default TeamRecord;
