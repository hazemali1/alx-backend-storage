-- procedure AddBonus
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name varchar(255), IN score INT)
BEGIN
	DECLARE project INT;
	if (SELECT COUNT(*) FROM projects WHERE name = project_name) <= 0 THEN
		INSERT INTO projects (name) VALUES (project_name);
	END IF;
	SELECT project_id INTO project FROM projects WHERE name = project_name;
	INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project, score);
END $$
DELIMITER ;
