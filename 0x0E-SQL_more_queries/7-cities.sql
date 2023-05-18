-- Script that creates hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Script that creates the cities
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL,
	FOREIGN KEY(state_id INT) NOT NULL,
	name VARCHAR(256)  NOT NULL
	);
