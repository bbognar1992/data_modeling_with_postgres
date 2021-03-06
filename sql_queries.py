# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(
songplay_id BIGSERIAL PRIMARY KEY, 
start_time int8, 
user_id int8, 
level varchar, 
song_id varchar, 
artist_id varchar, 
session_id int8, 
location varchar, 
user_agent varchar
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
user_id int8 PRIMARY KEY NOT NULL, 
first_name varchar, 
last_name varchar, 
gender varchar(1), 
level varchar
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(
song_id varchar PRIMARY KEY, 
title varchar NOT NULL, 
artist_id varchar, 
year int4, 
duration float
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
artist_id varchar PRIMARY KEY, 
name varchar NOT NULL, 
location varchar, 
latitude double precision, 
longitude double precision
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
start_time timestamp PRIMARY KEY NOT NULL, 
hour int2, 
day int2, 
week int2, 
month int2, 
year int2, 
weekday int2
);
""")

# INSERT RECORDS

songplay_table_insert = (""" 
INSERT INTO songplays (
start_time,  
user_id, 
level, 
song_id,  
artist_id, 
session_id,
location,
user_agent 
)
VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""
INSERT INTO users(
user_id, 
first_name, 
last_name, 
gender, 
level
) 
VALUES(%s,%s,%s,%s,%s) 
ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs(
song_id, 
title, 
artist_id, 
year, 
duration
) 
values(%s,%s,%s,%s,%s) 
ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists(
artist_id, 
name, 
location, 
latitude, 
longitude
) 
values(%s,%s,%s,%s,%s) 
ON CONFLICT DO NOTHING;
""")

time_table_insert = ("""
INSERT INTO time(
start_time, 
hour, 
day, 
week, 
month, 
year, 
weekday
) 
values(%s,%s,%s,%s,%s,%s,%s) 
ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT s.artist_id, s.song_id
FROM songs s 
INNER JOIN artists a ON s.artist_id=a.artist_id
WHERE s.title like %s AND a.name like %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create,
                        time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
