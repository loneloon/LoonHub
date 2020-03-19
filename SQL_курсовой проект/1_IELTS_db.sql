drop DATABASE IF EXISTS ielts;
CREATE DATABASE ielts;
USE ielts;

drop table if exists users;
create table users (
	id serial primary key,
	login VARCHAR(100),
	password_hash VARCHAR(100),
	created_at DATETIME,
	updated_at DATETIME,
	email VARCHAR(100) UNIQUE NOT NULL,
	deposit DECIMAL(10,2)),
	is_deleted ENUM('0', '1');

drop table if exists profiles;
create table profiles (
	user_id BIGINT UNSIGNED,
	given_name VARCHAR(150),
	family_name VARCHAR(150),
	`d.o.b.` DATE,
	phone_number VARCHAR(50),
	hometown VARCHAR(100),
	address VARCHAR(200),
	created_at DATETIME,
	updated_at DATETIME,

	INDEX fullname_idx(given_name, family_name)
	);
	
drop table if exists centres;
create table centres (
	id serial primary key,
	name VARCHAR(50),

	INDEX centre_list_idx(name)
	);

drop table if exists cities;
create table cities (
	id serial primary key,
	name VARCHAR(100),
	centre_id BIGINT UNSIGNED,
	`type` ENUM('head', 'regional'),
	price_regular DECIMAL(10,2),
	
	INDEX ct_name_idx(name),
	INDEX ct_role_idx(`type`)
	);

drop table if exists sessions;
create table sessions (
	id serial primary key,
	`date` DATE,
	exam_id BIGINT UNSIGNED,
	centre_id BIGINT UNSIGNED,
	city_id BIGINT UNSIGNED,
	location_id BIGINT UNSIGNED,
	allocated INT,
	taken INT,
	created_at DATETIME,
	updated_at DATETIME);

drop table if exists candidates;
create table candidates (
	id serial primary key,
	user_id BIGINT UNSIGNED,
	session_id BIGINT UNSIGNED,
	exam_id BIGINT UNSIGNED,
	status ENUM('active', 'locked', 'cancelled'),
	payment_status ENUM('paid', 'awaiting payment'),
	payment_id BIGINT UNSIGNED DEFAULT NULL,
	created_at DATETIME,
	updated_at DATETIME);
	
drop table if exists results;
create table results (
	id serial primary key,
	candidate_id BIGINT UNSIGNED,
	session_id BIGINT UNSIGNED,
	listening TINYINT,
	reading TINYINT,
	writing TINYINT,
	speaking TINYINT,
	overall DECIMAL(1,1),
	trf_number VARCHAR(50));

drop table if exists verification;
create table verification (
	user_id BIGINT UNSIGNED,
	`type` ENUM('passport', 'national identity card'),
	id_number VARCHAR(50),
	expiry_date DATE,
	authority VARCHAR(50),
	filename VARCHAR(50),
	`size(mb)` DECIMAL(10,1),
	filepath VARCHAR(100),
	status ENUM('verified', 'unverified'),
	uploaded_at DATETIME,
	updated_at DATETIME);

drop table if exists invitations;
create table invitations (
	id serial primary key,
	candidate_id BIGINT UNSIGNED,
	sent_at DATETIME,
	status ENUM('confirmed', 'unconfirmed'));

drop table if exists submitted_results;
create table submitted_results (
	id serial primary key,
	results_id BIGINT UNSIGNED,
	org_id BIGINT UNSIGNED,
	submitted_at DATETIME);
	
drop table if exists locations;
create table locations (
	id serial primary key,
	name VARCHAR(100),
	city_id BIGINT UNSIGNED,
	address VARCHAR(250),
	max_allocation INT,

	INDEX loc_list_idx(city_id),
	INDEX loc_names_idx(name)
	);

drop table if exists payments;
create table payments (
	id serial primary key,
	candidate_id BIGINT UNSIGNED,
	amount DECIMAL(10,2),
	action_date DATE,
	in_out ENUM('deposited', 'withdrawn'),
	`type` ENUM('cash', 'offline', 'online'),
	purpose ENUM('registration', 'transfer', 'TRF issue', 'refund', 'EOR', 'unknown'),
	`extra` DECIMAL(10,2) DEFAULT NULL);


drop table if exists organizations;
create table organizations (
	id serial primary key,
	name VARCHAR(150),
	department VARCHAR(150),
	country VARCHAR(100),
	city VARCHAR(100),
	address VARCHAR(200),
	phone VARCHAR(50),
	email VARCHAR(50),
	
	INDEX org_list_idx(name)
	);

drop table if exists exams;
create TABLE exams (
	id serial primary key,
	`type` ENUM('regular', 'ukvi'),
	format ENUM('paper-based', 'computer-based', 'life skills'),
	module ENUM('Academic', 'General', 'A1', 'B1'));
	
	
ALTER TABLE ielts.verification ADD CONSTRAINT users_ver_FK FOREIGN KEY (user_id) REFERENCES ielts.users(id) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE ielts.payments ADD CONSTRAINT cand_pay_FK FOREIGN KEY (candidate_id) REFERENCES ielts.candidates(id) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE ielts.profiles ADD CONSTRAINT users_prof_FK FOREIGN KEY (user_id) REFERENCES ielts.users(id) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE ielts.candidates ADD CONSTRAINT users_cand_FK FOREIGN KEY (user_id) REFERENCES ielts.users(id) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE ielts.invitations ADD CONSTRAINT cand_inv_FK FOREIGN KEY (candidate_id) REFERENCES ielts.candidates(id) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE ielts.results ADD CONSTRAINT cand_res_FK FOREIGN KEY (candidate_id) REFERENCES ielts.candidates(id) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE ielts.candidates ADD CONSTRAINT pay_cand_FK FOREIGN KEY (payment_id) REFERENCES ielts.payments(id) ON UPDATE CASCADE;
ALTER TABLE ielts.candidates ADD CONSTRAINT sesh_cand_FK FOREIGN KEY (session_id) REFERENCES ielts.sessions(id) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE ielts.submitted_results ADD CONSTRAINT res_subm_FK FOREIGN KEY (results_id) REFERENCES ielts.results(id) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE ielts.results ADD CONSTRAINT sesh_res_FK FOREIGN KEY (session_id) REFERENCES ielts.sessions(id) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE ielts.submitted_results ADD CONSTRAINT org_subm_FK FOREIGN KEY (org_id) REFERENCES ielts.organizations(id) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE ielts.cities ADD CONSTRAINT centre_city_FK FOREIGN KEY (centre_id) REFERENCES ielts.centres(id) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE ielts.sessions ADD CONSTRAINT loc_sesh_FK FOREIGN KEY (location_id) REFERENCES ielts.locations(id) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE ielts.locations ADD CONSTRAINT city_loc_FK FOREIGN KEY (city_id) REFERENCES ielts.cities(id) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE ielts.sessions ADD CONSTRAINT city_sesh_FK FOREIGN KEY (city_id) REFERENCES ielts.cities(id) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE ielts.sessions ADD CONSTRAINT centre_sesh_FK FOREIGN KEY (centre_id) REFERENCES ielts.centres(id) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE ielts.sessions ADD CONSTRAINT exam_type_FK1 FOREIGN KEY (exam_id) REFERENCES ielts.exams(id) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE ielts.candidates ADD CONSTRAINT exam_type_FK2 FOREIGN KEY (exam_id) REFERENCES ielts.exams(id) ON DELETE RESTRICT ON UPDATE CASCADE;














