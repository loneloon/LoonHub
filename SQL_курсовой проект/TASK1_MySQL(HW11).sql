-- Создайте таблицу logs типа Archive. Пусть при каждом создании записи в таблицах users, catalogs и products 
-- в таблицу logs помещается время и дата создания записи, название таблицы, идентификатор первичного ключа 
-- и содержимое поля name.

use shop;

-- Создаём отдельную таблицу для логов

DROP TABLE IF EXISTS logs;
CREATE TABLE logs (
	table_name ENUM ('users', 'products', 'catalogs'),
	id BIGINT UNSIGNED,
	name VARCHAR (255) NOT NULL,
	`date` DATETIME
	) COMMENT = 'Log records' ENGINE=Archive;

-- Создаём триггер по вставкам в таблицу users

DROP TRIGGER IF EXISTS users_log;
DELIMITER //
CREATE TRIGGER users_log BEFORE INSERT ON shop.users
FOR EACH ROW BEGIN
	INSERT INTO logs SET
		table_name = 'users',
		id = (SELECT NEW.id),
		name = (SELECT NEW.name),
		`date` = (SELECT NEW.updated_at);
END//
DELIMITER ;	

-- Создаём триггер по вставкам в таблицу products

DROP TRIGGER IF EXISTS products_log;
DELIMITER //
CREATE TRIGGER products_log BEFORE INSERT ON shop.products
FOR EACH ROW BEGIN
	INSERT INTO logs SET
		table_name = 'products',
		id = (SELECT NEW.id),
		name = (SELECT NEW.name),
		`date` = (SELECT NEW.updated_at);
END//
DELIMITER ;	

-- Создаём триггер по вставкам в таблицу catalogs

DROP TRIGGER IF EXISTS catalogs_log;
DELIMITER //
CREATE TRIGGER catalogs_log BEFORE INSERT ON shop.catalogs
FOR EACH ROW BEGIN
	INSERT INTO logs SET
		table_name = 'catalogs',
		id = (SELECT NEW.id),
		name = (SELECT NEW.name),
		`date` = (SELECT NOW());
END//
DELIMITER ;	

-- Тестируем триггеры

INSERT INTO users VALUES (7, 'name', '1990-10-10', NOW(), NOW());
INSERT INTO catalogs VALUES (6, 'Устройства ввода');
INSERT INTO products VALUES (8, 'Razer DeathAdder', 'Компьютерная мышь игровая', 5650, 6, NOW(),NOW());

SELECT * FROM logs;
