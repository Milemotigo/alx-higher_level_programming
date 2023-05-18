-- Script that creates hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Script that creates the cities
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL,
	state_id INT FOREIGN KEY(state_id) REFERENCES states(state_id) NOT NULL,
	name VARCHAR(256)  NOT NULL
	);
