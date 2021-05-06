CREATE DATABASE cars_api;
CREATE USER test WITH PASSWORD 'test';
GRANT ALL PRIVILEGES ON DATABASE "cars_api" to test;
-- #\i create_tables.sql
