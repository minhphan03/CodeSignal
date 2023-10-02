CREATE PROCEDURE solution()
BEGIN
	SELECT Name, ID 
	FROM Grades 
	WHERE (Final > Final * 0.5 + 0.25 * Midterm1 + 0.25 * Midterm2) and (Final > Midterm1 * 0.5 + Midterm2 * 0.5)
	ORDER BY SUBSTRING(Name, 1, 3) ASC, ID ASC;
END