DROP DATABASE IF EXISTS movr CASCADE; 

CREATE DATABASE movr;

CREATE USER app_user;

GRANT SELECT, INSERT, UPDATE, DELETE ON DATABASE movr TO app_user;

IMPORT TABLE movr.vehicles (
        id UUID PRIMARY KEY,
        last_longitude FLOAT8,
        last_latitude FLOAT8,
        battery INT8,
        last_checkin TIMESTAMP,
        in_use BOOL,
        vehicle_type STRING NOT NULL
    )
CSV DATA ('https://cockroach-university-public.s3.amazonaws.com/10000vehicles.csv')
    WITH delimiter = '|';

CREATE INDEX ON movr.vehicles (battery);

CREATE TABLE movr.location_history (
    id UUID PRIMARY KEY,
    vehicle_id UUID REFERENCES vehicles(id) ON DELETE CASCADE,
    ts TIMESTAMP NOT NULL,
    longitude FLOAT8 NOT NULL,
    latitude FLOAT8 NOT NULL
);

INSERT INTO movr.location_history (id, vehicle_id, ts, longitude, latitude)
    SELECT gen_random_uuid(), id, last_checkin, last_longitude, last_latitude FROM movr.vehicles;

SET sql_safe_updates = false;

ALTER TABLE movr.vehicles DROP COLUMN last_checkin,
                          DROP COLUMN last_longitude,
                          DROP COLUMN last_latitude;

SET sql_safe_updates = true;

CREATE TABLE movr.users(
    email STRING PRIMARY KEY, 
    last_name STRING, 
    first_name STRING
);

ALTER TABLE movr.users ADD COLUMN phone_numbers STRING ARRAY;

CREATE TABLE movr.rides (
    id UUID PRIMARY KEY, 
    vehicle_id UUID REFERENCES vehicles (id), 
    user_email STRING REFERENCES users (email), 
    start_ts TIMESTAMP, 
    end_ts TIMESTAMP
);

IMPORT INTO movr.users (
    email,
    last_name,
    first_name,
    phone_numbers
) 
CSV DATA ('https://cockroach-university-public.s3.amazonaws.com/10000_user_data.csv')  
    WITH delimiter = '|';

IMPORT INTO movr.rides (
    id,
    vehicle_id,
    user_email,
    start_ts,
    end_ts
    ) CSV DATA ('https://cockroach-university-public.s3.amazonaws.com/10000_rides_data.csv')
WITH delimiter = '|';