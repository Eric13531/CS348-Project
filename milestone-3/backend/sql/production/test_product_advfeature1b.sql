SELECT
    p.player_id,
    p.name,
    MATCH(p.name) AGAINST ("Stephen" IN NATURAL LANGUAGE MODE) AS relevance
FROM Player p
HAVING relevance > 0
ORDER BY relevance DESC
LIMIT 20;