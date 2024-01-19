-- Average weighted score
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_idd INT)
BEGIN
	DECLARE num INT DEFAULT 0;
	DECLARE sum INT DEFAULT 0;
	DECLARE mul INT DEFAULT 0;
	DECLARE res INT DEFAULT 0;

	DECLARE mycursor CURSOR FOR SELECT id, weight FROM projects;
	OPEN mycursor;
	FETCH NEXT FROM mycursor INTO @myid, @myweight;

	WHILE @@FETCH_STATUS = 0 DO
		SELECT (score * @myweight) INTO mul FROM corrections WHERE project_id = @myid AND user_id = user_idd;
		sum = sum + mul
		num = num + @myweight
		FETCH NEXT FROM mycursor INTO @myid, @myweight;
	END WHILE;

	CLOSE mycursor;
	DEALLOCATE mycursor;

	SET res = sum / num;
	UPDATE users SET average_score = res WHERE id = user_idd;
END $$
DELIMITER ;
