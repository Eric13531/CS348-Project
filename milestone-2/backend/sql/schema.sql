CREATE DATABASE IF NOT EXISTS cs348_nba
    CHARACTER SET utf8mb4 -- Western characters
    COLLATE utf8mb4_0900_ai_ci; -- So that comparisons are not case sensitive

USE cs348_nba;

CREATE TABLE Team (
    team_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    abbreviation VARCHAR(100) NOT NULL,
    conference VARCHAR(100) NOT NULL,
    wins INT NOT NULL,
    standing INT NOT NULL,

    CONSTRAINT uq_team_abbrev UNIQUE (abbreviation),
    CONSTRAINT uq_team_city_name UNIQUE (city, name)
);

CREATE TABLE Player (
    player_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    number INT NOT NULL,
    height VARCHAR(100) NULL,
    position VARCHAR(100) NULL,
    birthdate DATE NULL
);

CREATE TABLE TeamMember (
    player_id INT NOT NULL,
    team_id INT NOT NULL,

    PRIMARY KEY (player_id, team_id),
    FOREIGN KEY (player_id) REFERENCES Player(player_id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES Team(team_id) ON DELETE CASCADE
);

CREATE TABLE Game (
    game_id INT PRIMARY KEY AUTO_INCREMENT,
    date DATE NOT NULL,
    home_team INT NOT NULL,
    away_team INT NOT NULL,
    home_score INT DEFAULT 0,
    away_score INT DEFAULT 0,
    
    CONSTRAINT chk_teams_different CHECK (home_team <> away_team),
    FOREIGN KEY (home_team) REFERENCES Team(team_id) ON DELETE CASCADE,
    FOREIGN KEY (away_team) REFERENCES Team(team_id) ON DELETE CASCADE
);

CREATE TABLE PlayerStats (
    game_id INT NOT NULL,
    player_id INT NOT NULL,
    minutes INT DEFAULT NULL,
    points INT DEFAULT NULL,
    three_p INT DEFAULT NULL,
    assists INT DEFAULT NULL,
    steals INT DEFAULT NULL,
    blocks INT DEFAULT NULL,

    PRIMARY KEY (game_id, player_id),
    FOREIGN KEY (game_id) REFERENCES Game(game_id) ON DELETE CASCADE,
    FOREIGN KEY (player_id) REFERENCES Player(player_id) ON DELETE CASCADE
);