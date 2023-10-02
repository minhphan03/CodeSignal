CREATE PROCEDURE solution()
BEGIN
	SELECT DISTINCT subscribers.subscriber FROM (
		SELECT * FROM full_year
		UNION ALL
		SELECT * FROM half_year
	) subscribers 
	WHERE subscribers.newspaper LIKE '%Daily%'
	ORDER BY subscribers.subscriber;
END