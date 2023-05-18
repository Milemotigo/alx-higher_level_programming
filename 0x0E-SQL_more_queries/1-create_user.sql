-- script that creates the MySQL server user user_0d_1
-- Grant mysql user all privileges
IF NOT user_0d_1 EXISTS
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED WITH authentication_plugin BY 'user_0d_1_pwd'
GRANT user_0d_1*;
