-- Create out init db if it doesn't exist

CREATE DATABASE IF NOT EXISTS health_db;

-- Connect to the health_db
\c health_db

-- Create our table where we will load data from the source api if not exits
-- we can identify the colums from a sample data from the api

CREATE TABLE IF NOT EXISTS therapy_providers(
    enrollment_id VARCHAR(30),
    legal_business_name VARCHAR(100),
    street_address_line_1 VARCHAR(100),
    street_address_line_2 VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(2),
    zip_code VARCHAR(20),
    practice_location_phone_number VARCHAR(20),
    specialty_name VARCHAR(100),
    geographic_location_type_description VARCHAR(50),
    geographic_location_city_name VARCHAR(100),
    geographic_location_state_code VARCHAR(2),
    geographic_location_zip_code VARCHAR(20),
    state_county_name VARCHAR(50);
)