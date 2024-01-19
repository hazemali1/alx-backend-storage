-- function
CREATE FUNCTION SafeDiv(a int, b int)
	IF (b != 0) THEN
		RETURN a / b;
	ELSE
		RETURN 0
	END IF;
