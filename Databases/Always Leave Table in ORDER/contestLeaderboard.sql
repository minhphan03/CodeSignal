CREATE PROCEDURE solution()
BEGIN
	SELECT name from leaderboard
	ORDER BY score DESC LIMIT 3, 5;
END