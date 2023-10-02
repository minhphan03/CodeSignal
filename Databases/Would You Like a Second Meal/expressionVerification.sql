CREATE PROCEDURE solution()
BEGIN
	SELECT id, a, b, operation, c
	FROM (
		SELECT id, a, b, operation, c, IF (
			operation='+', a+b, IF(
				operation='-', a-b, IF (
					operation='*', a*b,
					a/b
				)
		)) as result
		FROM expressions
		
	
	) as compare
	WHERE compare.result = compare.c 
	ORDER BY id;
END

-----

CREATE PROCEDURE solution()
BEGIN
	select * 
        from expressions
        where elt(locate(operation, "+-*/"), a+b, a-b, a*b, a/b) = c;
END

