CREATE PROCEDURE solution()
BEGIN
	SELECT id, scholarship / 12
	FROM scholarships;
END