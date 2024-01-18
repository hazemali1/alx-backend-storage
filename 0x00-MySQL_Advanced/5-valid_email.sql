-- trigger for valid_email
DELIMITER $$
CREATE TRIGGER reset_email AFTER UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email != NEW.email
	THEN
		UPDATE users SET valid_email = 0 WHERE email = NEW.email;
	END IF;
END $$
DELIMITER ;
