CREATE PROCEDURE solution()
BEGIN
	SELECT id, name, surname
	FROM Suspect
	WHERE UPPER(name) LIKE 'B%' AND UPPER(surname) LIKE 'GRE_N' AND HEIGHT <= 170
	ORDER BY id ASC;
END