-- procedure AddBonus
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_idd INT)
BEGIN
	DECLARE n INT;
	DECLARE s INT;
	DECLARE a float;
	SELECT COUNT(*) INTO n FROM corrections WHERE user_id = user_idd;
	SELECT SUM(score) INTO s FROM corrections WHERE user_id = user_idd;
	SET a = s / n;
	UPDATE users SET average_score = a WHERE id = user_idd;
END $$
DELIMITER ;
