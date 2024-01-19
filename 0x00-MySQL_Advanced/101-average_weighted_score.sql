-- Average weighted score
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE user_idd INT;

	DECLARE num FLOAT DEFAULT 0;
	DECLARE sum FLOAT DEFAULT 0;
	DECLARE mul FLOAT DEFAULT 0;
	DECLARE res FLOAT DEFAULT 0;
	DECLARE myid INT;
	DECLARE counter INT;
	DECLARE myweight INT;
	DECLARE done INT DEFAULT 0;
	DECLARE id_list VARCHAR(255) DEFAULT '';


	

	DECLARE myuser CURSOR FOR SELECT id FROM users;
	

	
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

	OPEN myuser;
	FETCH NEXT FROM myuser INTO user_idd;

	my_loop_user: LOOP
        IF done THEN
            LEAVE my_loop_user;
        END IF;

		SET id_list = CONCAT(id_list, user_idd, ',');

		FETCH NEXT FROM myuser INTO user_idd;
	END LOOP my_loop_user;
	CLOSE myuser;


	DECLARE mycursor CURSOR FOR SELECT id, weight FROM projects;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

	SET counter := 1;
    SET user_idd := TRIM(SUBSTRING_INDEX(id_list, ',', counter));
    
    WHILE LENGTH(user_idd) > 0 DO
		my_loop: LOOP
			IF done THEN
				LEAVE my_loop;
			END IF;

			SELECT (score * myweight) INTO mul FROM corrections WHERE project_id = myid AND user_id = user_idd;
			SET sum = sum + mul;
			SET num = num + myweight;
			FETCH NEXT FROM mycursor INTO myid, myweight;
		END LOOP my_loop;

		SET counter := counter + 1;
        SET user_idd := TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(id_list, ',', counter), ',', -1));
    END WHILE;

		CLOSE mycursor;

		SET res = sum / num;
		UPDATE users SET average_score = res WHERE id = user_idd;

END $$
DELIMITER ;






