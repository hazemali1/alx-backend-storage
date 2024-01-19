-- function
DELIMITER $$
CREATE FUNCTION SafeDiv(a int, b int)
BEGIN
	RETURN IF (b != 0, a / b, 0)
END $$
DELIMITER ;
