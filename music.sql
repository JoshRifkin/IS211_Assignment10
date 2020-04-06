-- Assignment 10
-- Music DB
-- By: Joshua Rifkin

DROP TABLE IF EXISTS Artists;
DROP TABLE IF EXISTS Albums;
DROP TABLE IF EXISTS Songs;



CREATE TABLE Artists (
    artist_id INTEGER PRIMARY KEY,
    name VARCHAR(64) NOT NULL
);

CREATE TABLE Albums (
    album_id INTEGER PRIMARY KEY,
    artist_id INTEGER NOT NULL,
    artist_name VARCHAR(64)
);

CREATE TABLE Songs (
    song_id INTEGER PRIMARY KEY,
    album_id INTEGER NOT NULL,
    track_num INTEGER NOT NULL,
    playtime INTEGER NOT NULL
);