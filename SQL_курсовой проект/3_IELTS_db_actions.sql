use ielts;

# Процедура считает сдачу от оплаты за экзамен или недостающую сумму
	  
DROP PROCEDURE IF EXISTS calculate_payments;
DELIMITER //
CREATE PROCEDURE calculate_payments ()
BEGIN
	UPDATE payments SET 
		extra = amount - (SELECT price_regular FROM cities WHERE id in (SELECT city_id FROM sessions WHERE candidate_id = payments.candidate_id));
END//
DELIMITER ;

# Тест процедуры

INSERT INTO payments (id, candidate_id, amount, action_date, in_out, `type`, purpose) VALUES 
(1, 2, 13350, '2019-12-09', 'deposited', 'offline', 'registration'),
(2, 1, 14350, '2019-12-09', 'deposited', 'offline', 'registration');

CALL calculate_payments;

# Процедура обновляет баланс юзеров согласно информации по столбцу extra из таблицы оплат (payments)

DROP PROCEDURE IF EXISTS update_user_balance;
DELIMITER //
CREATE PROCEDURE update_user_balance ()
BEGIN
	UPDATE users SET 
		deposit = (SELECT extra FROM payments where candidate_id = (SELECT id from candidates where user_id = users.id));
END//
DELIMITER ;

CALL update_user_balance;

SELECT * FROM users where deposit;

# Процедура обновляем статус бронирований, на которые поступила оплата

DROP PROCEDURE IF EXISTS update_booking_status;
DELIMITER //
CREATE PROCEDURE update_booking_status ()
BEGIN
	IF 

# Триггер запрещающий создание бронирования на занятую сессию

 
DROP TRIGGER IF EXISTS full_session;
DELIMITER //
CREATE TRIGGER full_session BEFORE INSERT ON ielts.candidates
FOR EACH ROW BEGIN
	SET @sesh := NEW.session_id;
	SELECT taken INTO @taken FROM sessions WHERE id = @sesh;
	SELECT allocated INTO @alloc FROM sessions WHERE id = @sesh;
	IF @taken = @alloc THEN
  		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No available seats left!';	 
	END IF;	
END//
DELIMITER ;	

INSERT INTO sessions
 SET
 	id = 2,
 	`date` = '2019-12-15',
 	exam_id = 7,
 	centre_id = 2,
 	city_id = 3,
 	location_id = 1,
 	allocated = 15,
 	taken = 15,
 	created_at = NOW(),
 	updated_at = NOW();

INSERT INTO candidates
SET 
 	id = 3,
 	user_id = 21,
 	session_id = 2,
 	exam_id = 7,
 	status = 'active',
 	payment_status = 'awaiting payment',
 	payment_id = NULL,
 	created_at = NOW(),
 	updated_at = NOW();

# Триггер увеличивает счётчик занятых мест каждый раз когда создаётся бронирование на экзамен

DROP TRIGGER IF EXISTS booking_counter;
DELIMITER //
CREATE TRIGGER booking_counter AFTER INSERT ON ielts.candidates
FOR EACH ROW BEGIN
	SELECT taken INTO @bookings FROM ielts.sessions WHERE sessions.id = (SELECT session_id from candidates where candidates.id = NEW.id);
	UPDATE sessions SET taken = (SELECT @bookings + 1) WHERE sessions.id = (SELECT session_id from candidates where candidates.id = NEW.id);
END//
DELIMITER ;	

DELETE FROM candidates where id = 3;

 INSERT INTO candidates
 SET 
 	id = 4,
 	user_id = 19,
 	session_id = 1,
 	exam_id = 3,
 	status = 'active',
 	payment_status = 'awaiting payment',
 	payment_id = NULL,
 	created_at = NOW(),
 	updated_at = NOW();



 
 
 