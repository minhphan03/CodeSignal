CREATE PROCEDURE solution()
BEGIN
	SELECT WEEKDAY(mischief_date) AS weekday, mischief_date, author, title
	FROM mischief
	ORDER BY weekday ASC, FIELD(author, "Huey",  "Dewey", "Louie"), mischief_date, title ASC;
END