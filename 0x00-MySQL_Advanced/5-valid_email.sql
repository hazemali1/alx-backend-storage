-- trigger for valid_email
DELIMITER $$
CREATE TRIGGER reset_email AFTER UPDATE ON users
FOR EACH ROW
BEGIN
	UPDATE users SET valid_email = 0 WHERE OLD.email != NEW.email;
END $$
DELIMITER ;
