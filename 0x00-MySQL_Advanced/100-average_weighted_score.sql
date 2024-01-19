-- Average weighted score
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_idd INT)
BEGIN
	DECLARE num INT DEFAULT 0;
	DECLARE sum INT DEFAULT 0;
	DECLARE mul INT DEFAULT 0;
	DECLARE res INT DEFAULT 0;
	DECLARE myid INT;
    DECLARE myweight INT;
	DECLARE done INT DEFAULT 0;

	DECLARE mycursor CURSOR FOR SELECT id, weight FROM projects;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
	OPEN mycursor;
	FETCH NEXT FROM mycursor INTO myid, myweight;

	my_loop: LOOP
        IF done THEN
            LEAVE my_loop;
        END IF;

		SELECT (score * @myweight) INTO mul FROM corrections WHERE project_id = myid AND user_id = user_idd;
		SET sum = sum + mul;
		SET num = num + myweight;
		FETCH NEXT FROM mycursor INTO myid, myweight;
	END LOOP my_loop;

	CLOSE mycursor;
	DEALLOCATE mycursor;

	SET res = sum / num;
	UPDATE users SET average_score = res WHERE id = user_idd;
END $$
DELIMITER ;
