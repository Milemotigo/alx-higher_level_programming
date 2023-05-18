-- Script that creates the table id_not_null
CREATE TABLE IF NOT EXISTS unique_id(
	id INT UNIQUE PRIMARY KEY NOT NULL,
	name VARCHAR(256)  NOT NULL
	);
