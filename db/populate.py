import psycopg2

NAMES = False
TITLES = False
PRINCIPALS = False
TITLES_BASE = True

if NAMES:
    conn = psycopg2.connect("dbname=moviegame user=postgres")
    cur = conn.cursor()

    line_counter = 0
    for line in open("data/name.basics.tsv"):
        if line_counter > 0:
            print(line.split())
            fields = line.split("\t")
            cur.execute("INSERT INTO names (nconst, primaryName, birthYear, deathYear, primaryProfession, knownForTitles) VALUES (%s, %s, %s, %s, %s, %s)", tuple(fields) )
        line_counter += 1

    conn.commit()
    cur.close()
    conn.close()

if TITLES:
    conn = psycopg2.connect("dbname=moviegame user=postgres")
    cur = conn.cursor()

    line_counter = 0
    for line in open("data/title.akas.tsv"):
        if line_counter > 0:
            print(line.split())
            fields = line.split("\t")
            cur.execute("INSERT INTO titles (titleId, ordering, title, region, language, types, attributes, isOriginalTitle) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", tuple(fields) )
        line_counter += 1

    conn.commit()
    cur.close()
    conn.close()

if PRINCIPALS:
    conn = psycopg2.connect("dbname=moviegame user=postgres")
    cur = conn.cursor()

    line_counter = 0
    for line in open("data/title.principals.tsv"):
        if line_counter > 0:
            print(line.split())
            fields = line.split("\t")
            cur.execute("INSERT INTO titles_principals (tconst, ordering, nconst, category, job, characters) VALUES (%s, %s, %s, %s, %s, %s)", tuple(fields) )
        line_counter += 1

    conn.commit()
    cur.close()
    conn.close()

if TITLES_BASE:
    conn = psycopg2.connect("dbname=moviegame user=postgres")
    cur = conn.cursor()
#  tconst	titleType	primaryTitle	originalTitle	isAdult	startYear	endYear	runtimeMinutes	genres
    line_counter = 0
    for line in open("data/title.basics.tsv"):
        if line_counter > 0:
            print(line.split())
            fields = line.split("\t")
            cur.execute("INSERT INTO titles_base (tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple(fields) )
        line_counter += 1

    conn.commit()
    cur.close()
    conn.close()
