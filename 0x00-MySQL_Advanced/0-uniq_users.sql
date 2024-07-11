-- SQL script that creates a table users
-- If the table already exists, your script should not fail
CREATE TABLE IF NOT EXISTS users (
	id INT PRIMARY KEY AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name VARCHAR(255) NOT NULL
);
