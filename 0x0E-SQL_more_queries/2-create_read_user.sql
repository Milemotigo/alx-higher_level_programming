-- Script that creates the MySQL server user user_0d_2,  htbn_0d_2
-- Grant mysql user all privileges
CREATE DATABASE IF NOT EXISTS htbn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON htbn_0d_2.* TO user_0d_2@localhost;
