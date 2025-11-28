import { useEffect, useState } from "react";
import axios from "axios";
import './App.css';
import PlayerList from "./components/PlayerList";
import TeamList from "./components/TeamList";
import GameList from "./components/GameList";


function App() {
  const [test, setTest] = useState("");

  useEffect(() => {
    axios.get(`${process.env.REACT_APP_API_URL}`)
      .then((res) => setTest(res.data.message))
      .catch((err) => console.log("API error:", err))
  }, []);

  return (
    <div className="App">
      <h1>NBA Player Stats 2024-25</h1>
      {/* <p>Backend test: {test}</p> */}
      <PlayerList />
      <TeamList />
      <GameList/>
    </div>
  );
}

export default App;
