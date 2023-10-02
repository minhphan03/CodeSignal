CREATE PROCEDURE solution()
BEGIN
	SELECT id, name, surname
	FROM Suspect
	WHERE (height <= 170) OR (UPPER(name) NOT LIKE 'B%') OR (UPPER(surname) NOT LIKE 'GRE_N')
	ORDER BY id ASC;
END