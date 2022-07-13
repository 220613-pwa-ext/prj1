DROP TABLE IF EXISTS ers_users;
DROP TABLE IF EXISTS ers_status_types;
DROP TABLE IF EXISTS ers_reimbursement_types;
DROP TABLE IF EXISTS ers_reimbursement;
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
	resolved TIMESTAMP NOT NULL,
	status_id INT NOT NULL,
	type_id INT NOT NULL,
	description VARCHAR(50) NOT NULL,
	receipt BYTEA NOT NULL,
	author_id INT NOT NULL,
	resolver_id INT NOT NULL,
	CONSTRAINT fk_author_id
  		FOREIGN KEY (author_id) REFERENCES "ers_users" (id),
  	CONSTRAINT fk_resolver_id
  		FOREIGN KEY (resolver_id) REFERENCES "ers_users" (id),
  	CONSTRAINT fk_status_id
  		FOREIGN KEY (status_id) REFERENCES "ers_status_types" (id),
  	CONSTRAINT fk_type_id
  		FOREIGN KEY (type_id) REFERENCES "ers_reimbursement_types" (id)

);

INSERT INTO ers_roles (role_name) VALUES ('finance_manager'), ('employee');

INSERT INTO ers_users (username, pass, first_name, last_name, email, user_role_id)
	VALUES 	('JohnD80','$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2','John','Doe','jd@a.ca',2);
--			('Jane','Doe','1981-01-01','2003-01-02','j@a.ca', 'M2J 1M5', '551', '555-555-5001'),
--			('Johny','Doe','2000-01-01','2020-01-03','jhy@a.ca', 'M2J 1M5', '553', '555-555-5003'),
--			('John1','Doe1','1980-01-01','2000-01-01','jd@a.ca', 'M2J 1M5', '554', '555-555-5004'),
--			('Jane1','Doe1','1981-01-01','2003-01-02','j@a.ca', 'M2J 1M5', '555', '555-555-5005'),
--			('Johny1','Doe1','2000-01-01','2020-01-03','jhy@a.ca', 'M2J 1M5', '556', '555-555-5006'),
--			('John2','Doe','1980-01-01','2000-01-01','jd@a.ca', 'M2J 1M5', '557', '555-555-5007'),
--			('Jane2','Doe','1981-01-01','2003-01-02','j@a.ca', 'M2J 1M5', '558', '555-555-5008'),
--			('Johny2','Doe','2000-01-01','2020-01-03','jhy@a.ca', 'M2J 1M5', '559', '555-555-5009');
		
SELECT * FROM ers_users;
