-- trigger quantity
DELIMITER $$
CREATE TRIGGER quantity AFTER INSERT ON orders
BEGIN
	UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
END $$
DELIMITER;
