/* 
enter the docker container 'docker exec -it weather_db bash'
enter database with this command 'psql -U user -d database_name' or 'psql -U user -d database_name -f script_file.sql'
run the psql script in psql interactive mode '\i path/to/script/'
to copy data from container to host direcrory docker cp weather_db:/var/lib/postgresql/data /path/to/host/directory
*/

CREATE TABLE IF NOT EXISTS nairobi_weather_data (
    datetime TIMESTAMP PRIMARY KEY,
    tempmax NUMERIC(5, 2),
    tempmin NUMERIC(5, 2),
    temp NUMERIC(5, 2),
    feelslikemax NUMERIC(5, 2),
    feelslikemin NUMERIC(5, 2),
    feelslike NUMERIC(5, 2),
    dew NUMERIC(5, 2),
    humidity NUMERIC(5, 2),
    precip NUMERIC(5, 2),
    precipprob INTEGER,
    precipcover NUMERIC(5, 2),
    preciptype TEXT[],
    snow INTEGER,
    snowdepth INTEGER,
    windgust NUMERIC(5, 2),
    windspeed NUMERIC(5, 2),
    winddir NUMERIC(5, 2),
    sealevelpressure NUMERIC(7, 2),
    cloudcover NUMERIC(5, 2),
    visibility NUMERIC(5, 2),
    solarradiation NUMERIC(5, 2),
    solarenergy NUMERIC(5, 2),
    uvindex INTEGER,
    severerisk INTEGER,
    sunrise TIMESTAMP,
    sunset TIMESTAMP,
    moonphase NUMERIC(3, 2),
    conditions TEXT,
    description TEXT,
    icon TEXT,
    stations TEXT[]
);

COPY nairobi_weather_data (
  datetime,tempmax,tempmin,temp,feelslikemax,
  feelslikemin,feelslike,dew,humidity,precip,
  precipprob,precipcover,preciptype,snow,snowdepth
  ,windgust,windspeed,winddir,sealevelpressure,
  cloudcover,visibility,solarradiation,solarenergy,
  uvindex,severerisk,sunrise,sunset,moonphase,
  conditions,description,icon,stations
  )
  
FROM '/var/lib/postgresql/data/nairobi_weather_script.sql'
WITH (FORMAT csv, DELIMITER ',', HEADER true);