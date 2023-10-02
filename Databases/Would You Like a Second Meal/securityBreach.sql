CREATE PROCEDURE solution()
BEGIN
	SELECT *
	FROM users
	WHERE BINARY attribute LIKE CONCAT("_%", "\%", first_name, "_", second_name, "\%", "%")
	ORDER BY attribute ASC;
END;

-- for case-sensitive LIKE operators, use BINARY keyword in WHERE
--The BINARY operator is deprecated as of MySQL 8.0.27, and you should expect its removal in a future version of MySQL. Use CAST(... AS BINARY) instead.