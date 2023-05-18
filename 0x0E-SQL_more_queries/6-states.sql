-- Script that creates the table id_not_null
CREATE TABLE IF NOT EXISTS states(
	id INT AUTO_INCREMENT  UNIQUE PRIMARY KEY NOT NULL,
	name VARCHAR(256)  NOT NULL
	);
