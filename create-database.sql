CREATE DATABASE catcollector;

CREATE USER cat_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE catcollector TO cat_admin;