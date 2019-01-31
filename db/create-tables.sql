CREATE DATABASE IF NOT EXISTS moviegame;

CREATE TABLE names(
    nconst VARCHAR,
    primaryName VARCHAR,
    birthYear VARCHAR,
    deathYear VARCHAR,
    primaryProfession VARCHAR,
    knownForTitles VARCHAR
);

CREATE UNIQUE INDEX idx_names_id ON names (nconst);


CREATE TABLE titles(
    titleId VARCHAR,
    ordering INT,
    title VARCHAR,
    region VARCHAR,
    language VARCHAR,
    types VARCHAR,
    attributes VARCHAR,
    isOriginalTitle VARCHAR
);

CREATE INDEX idx_title_id ON titles (titleId);

CREATE TABLE titles_principals(
    tconst VARCHAR,
    ordering VARCHAR,
    nconst VARCHAR,
    category VARCHAR,
    job VARCHAR,
    characters VARCHAR
);

CREATE INDEX idx_titles_principals_name_id ON titles_principals (nconst);
CREATE INDEX idx_titles_principals_title_id ON titles_principals (tconst);


-- tconst	titleType	primaryTitle	originalTitle	isAdult	startYear	endYear	runtimeMinutes	genres

CREATE TABLE titles_base(
    tconst VARCHAR,
    titleType VARCHAR,
    primaryTitle VARCHAR,
    originalTitle VARCHAR,
    isAdult VARCHAR,
    startYear VARCHAR,
    endYear VARCHAR,
    runtimeMinutes VARCHAR,
    genres VARCHAR
);

CREATE INDEX idx_titles_base_title_id ON titles_base (tconst);

-- Full text searches:

CREATE INDEX idx_full_text_titles ON titles_base USING GIN (to_tsvector('english', primaryTitle));
CREATE INDEX idx_full_text_names ON names USING GIN (to_tsvector('english', primaryName));

