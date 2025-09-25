## Setup Instructions

### 1. Clone the Repository
```bash
git clone git@github.com:Eric13531/CS348-Project.git
cd CS348-Project
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
