import React, { useEffect, useState } from "react";
import api from "../utils/api";
import GameStats from "./GameStats";

const GameList = () => {
  const [games, setGames] = useState([]);
  const [selectedGame, setSelectedGame] = useState(null);
  const [isListOpen, setIsListOpen] = useState(true);

  useEffect(() => {
    const fetchGames = async () => {
      try {
        const response = await api.get("/games/");
        setGames(response.data.data);
        console.log("Fetched games");
      } catch (error) {
        console.error("Error fetching games:", error);
      }
    };
    fetchGames();
  }, []);

  return (
    <div>
      <h2>Games</h2>
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
        {isListOpen ? "Hide game list ▲" : "Show game list ▼"}
      </button>
      {isListOpen && (
      <div style={{ display: "flex", "flex-wrap": "wrap", gap: "10px", "justify-content": "center" }}>
        {games.map((game) => (
          <button
            key={game.game_id}
            onClick={() => setSelectedGame(game)}
          >
            {game.date}, {game.home_abb} vs {game.away_abb}
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
        {isListOpen ? "Hide game list ▲" : "Show game list ▼"}
      </button>

      {selectedGame && (
        <GameStats gameId={selectedGame.game_id}/>
      )}
    </div>
  );
};

export default GameList;