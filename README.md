## Setup Instructions

### 1. Clone the Repository
```bash
git clone git@github.com:Eric13531/CS348-Project.git
cd CS348-Project/milestone-0
```

### 2. Start the Backend

```bash
cd backend
python -m venv .cs348env
source .cs348env/bin/activate # Mac/Linux
.cs348env\Scripts\activate # Windows

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend will be running at `http://127.0.0.1:8000`

You should replace the fields in DB_CONFIG to suit your system and connect to local mysql instance

To create the database and load the sample database, simply create your database in mysql,
run `backend/sql/schema.sql` to set up the tables, and `backend/sql/player_insert.sql`, 
`backend/sql/team_insert.sql`, `backend/sql/game_insert.sql`, `backend/sql/team_member_insert.sql`, 
`backend/sql/player_stats_insert.sql`

Currently, our application only supports seeing all the stat averages of the players in our sample database.
We have a sample feature defined in `backend/sql/feature1_sample.sql` which produced the output file 
`backend/sql/feature1_output.csv`, a similar function is coded and accessible through our backend.

You can also see the player_id and player names of all players in our sample database using `http://127.0.0.1:8000/players/`

We have implemented our first feature, which shows the averages of a player given player_id, 
You can see it by visiting `http://127.0.0.1:8000/player_averages/?player_id=1`

Running the React app and setting the app URL to `http://127.0.0.1:8000` will run the frontend

Here are the expected results:

![Screenshot of Players and Stats](screenshots/player_stats.png)

### 3. Start the Frontend

```bash
cd ../frontend
npm install

npm start
```

Frontend will be running at: `http://localhost:3000`

### 4. Set up Environment Variables

`frontend/.env`
```ini
REACT_APP_API_URL=http://127.0.0.1:8000
```
