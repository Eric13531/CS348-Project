ALTER TABLE Player
ADD FULLTEXT INDEX idx_player_name (name);