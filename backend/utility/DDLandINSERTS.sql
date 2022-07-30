DROP TABLE IF EXISTS ers_reimbursements;
DROP TABLE IF EXISTS ers_users;
DROP TABLE IF EXISTS ers_roles;
DROP TABLE IF EXISTS ers_status_types;
DROP TABLE IF EXISTS ers_reimbursement_types;

--CREATE EXTENSION pgcrypto;

CREATE TABLE ers_roles (
	id SERIAL PRIMARY KEY,
	role_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE ers_users(
	id SERIAL PRIMARY KEY,
	username VARCHAR(20) NOT NULL,
	pass VARCHAR(60) NOT NULL,
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	email VARCHAR(30) NOT NULL,
	user_role_id INT NOT NULL,
	CONSTRAINT fk_user_role_id
  		FOREIGN KEY (user_role_id) REFERENCES "ers_roles" (id)
);


CREATE TABLE ers_status_types (
	id SERIAL PRIMARY KEY,
	status_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE ers_reimbursement_types (
	id SERIAL PRIMARY KEY,
	reimb_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE ers_reimbursements (
	id SERIAL PRIMARY KEY,
	amount NUMERIC NOT NULL,
	submitted TIMESTAMP NOT NULL,
	resolved TIMESTAMP,
	status_id INT NOT NULL,
	type_id INT NOT NULL,
	description VARCHAR(500) NOT NULL,
	receipt BYTEA NOT NULL,
	author_id INT NOT NULL,
	resolver_id INT ,
	CONSTRAINT fk_author_id
  		FOREIGN KEY (author_id) REFERENCES "ers_users" (id),
  	CONSTRAINT fk_resolver_id
  		FOREIGN KEY (resolver_id) REFERENCES "ers_users" (id),
  	CONSTRAINT fk_status_id
  		FOREIGN KEY (status_id) REFERENCES "ers_status_types" (id),
  	CONSTRAINT fk_type_id
  		FOREIGN KEY (type_id) REFERENCES "ers_reimbursement_types" (id)

);

INSERT INTO ers_roles (role_name) VALUES ('finance_manager'), ('employee'), ('IT_admin');
SELECT * FROM ers_roles;

INSERT INTO ers_users (username, pass, first_name, last_name, email, user_role_id)
	VALUES 	('JohnD80','$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2','John','Doe','jd@a.ca',2),
			('JaneD80','$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2','Jane','Doe','jd@a.ca',2),
			('JonD80','$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2','Johny','Doe','jd@a.ca',2),
			('valiv9','$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2','Valentin','Vlad','vv@a.ca',1),
			('willrock22','$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2','Cam','Coder','jd@a.ca',1);
		
SELECT * FROM ers_users;

INSERT INTO ers_status_types (status_name) VALUES ('pending'), ('approved'),('denied');
SELECT * FROM ers_status_types;

INSERT INTO ers_reimbursement_types (reimb_name) VALUES ('Lodging'), ('Travel'), ('Food'),('Other');
SELECT * FROM ers_reimbursement_types;

--INSERT INTO ers_reimbursements (amount, submitted, status_id, type_id, description, receipt, author_id) 
--	VALUES	(500, Now(), 1, 1, 'Staying at hotel due to extended business meeting', (), 1),
--			(600, Now(), 1, 2, 'Travel to Vancouver', bytea(''), 1),
--			(700, Now(), 1, 3, 'Eat crackers', bytea(''), 1),
--			(800, Now(), 1, 4, 'Make peace with spouse after late business meeting', bytea(''), 1),
--			(900, Now(), 1, 1, 'Staying at hotel due to extended business meeting', bytea(''), 2),
--			(1000, Now(), 1, 2, 'Travel to Vancouver', bytea(''), 2),
--			(1100, Now(), 1, 3, 'Eat crackers', bytea(''), 2),
--			(1200, Now(), 1, 4, 'Make peace with spouse after late business meeting', bytea(''), 2),
--			(400, Now(), 1, 1, 'Staying at hotel due to extended business meeting', bytea(''), 3),
--			(300, Now(), 1, 2, 'Travel to Vancouver', bytea(''), 3),
--			(200, Now(), 1, 3, 'Eat crackers', bytea(''), 3),
--			(100, Now(), 1, 1, 'Staying at hotel due to extended business meeting', bytea(''), 4),
--			(100, Now(), 1, 1, 'Staying at hotel due to extended business meeting', bytea(''), 4),
--			(500, Now(), 1, 2, 'Travel to Vancouver', bytea(''), 5),
--			(500, Now(), 1, 1, 'Staying at hotel due to extended business meeting', bytea(''), 5),
--			(500, Now(), 1, 3, 'Eat crackers', bytea(''), 5);

SELECT * FROM ers_reimbursements ;
SELECT r.id, r.amount, r.submitted, est.status_name, ert.reimb_name, r.description, r.receipt, CONCAT(eu.first_name , ' ', eu.last_name) AS employee_name 
FROM ers_reimbursements r 
JOIN ers_status_types est ON r.status_id = est.id 
JOIN ers_reimbursement_types ert ON r.type_id = ert.id
JOIN ers_users eu ON r.author_id = eu.id
WHERE r.author_id <> 5;
SELECT r.id, r.amount, r.submitted, est.status_name, ert.reimb_name, r.description, r.receipt, CONCAT(eu.first_name , ' ', eu.last_name) AS employee_name 
FROM ers_reimbursements r 
JOIN ers_status_types est ON r.status_id = est.id 
JOIN ers_reimbursement_types ert ON r.type_id = ert.id
LEFT JOIN ers_users eu ON r.resolver_id = eu.id
WHERE r.author_id = 5;
--SELECT  r.receipt 
--FROM ers_reimbursements r 
--JOIN ers_status_types est ON r.status_id = est.id 
--JOIN ers_reimbursement_types ert ON r.type_id = ert.id
--JOIN ers_users eu ON r.author_id = eu.id
--WHERE r.author_id = 5 and r.id = 28;
up