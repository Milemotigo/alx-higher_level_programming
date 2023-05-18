-- Script that creates hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
-- Scripit that creates the cities
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	PRIMARY KEY(id),
	state_id INT NOT NULL,
	FOREIGN KEY(state_id),
	REFERENCES states(state_id) NOT NULL
	);
