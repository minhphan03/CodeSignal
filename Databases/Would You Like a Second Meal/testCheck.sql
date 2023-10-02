CREATE PROCEDURE solution()
    SELECT id, IF (ISNULL(given_answer), "no answer", IF (given_answer = correct_answer, "correct","incorrect")) AS checks
    FROM answers
    ORDER BY id;
