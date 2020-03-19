use ielts;

# Список городов с указанием названий центров, к которым они принадлежат, с использованием JOIN

SELECT cities.id, cities.name,  centres.name as 'centre', cities.`type`, cities.price_regular
FROM cities
INNER JOIN centres ON centres.id = cities.centre_id;


# 1-ое представление: детальное отображение информации по сессиям

DROP VIEW IF EXISTS exam_sessions;
CREATE VIEW exam_sessions AS
SELECT
	id,
	`date`, 
	(select `type` FROM exams WHERE id = sessions.exam_id) as 'type',
	(select `format` FROM exams WHERE id = sessions.exam_id) as 'format',
	(select `module` FROM exams WHERE id = sessions.exam_id) as 'module',
	(select name from centres where id = sessions.centre_id) as 'centre',
	(select name from cities where id = sessions.city_id) as 'city',
	(select name from locations where id = sessions.location_id) as 'location',
	allocated,
	taken,
	updated_at
FROM sessions;

SELECT * FROM exam_sessions;

# 2-ое представление: детальное отображение информации по "букингам"

DROP VIEW IF EXISTS candidates_info;
CREATE VIEW candidates_info AS
SELECT 
	(SELECT given_name FROM profiles where user_id = candidates.user_id) as 'given name',
	(SELECT family_name FROM profiles where user_id = candidates.user_id) as 'family name',
	(SELECT `date` FROM sessions where id = session_id) as 'date',
	(select name from cities where id = (select city_id from sessions where id = candidates.session_id)) as 'city',
	(select `type` FROM exams WHERE id = exam_id) as 'type',
	(select `format` FROM exams WHERE id = exam_id) as 'format',
	(select `module` FROM exams WHERE id = exam_id) as 'module',
	payment_status,
	updated_at
FROM candidates;

SELECT * FROM candidates_info;