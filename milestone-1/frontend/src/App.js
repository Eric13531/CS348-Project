import { useEffect, useState } from "react";
import axios from "axios";
import './App.css';
import PlayerList from "./components/PlayerList";


function App() {
  const [test, setTest] = useState("");

  useEffect(() => {
    axios.get(`${process.env.REACT_APP_API_URL}`)
      .then((res) => setTest(res.data.message))
      .catch((err) => console.log("API error:", err))
  }, []);

  return (
    <div className="App">
      <h1>NBA Player Stats</h1>
      <p>Backend test: {test}</p>
      <PlayerList />
    </div>
  );
}

export default App;
