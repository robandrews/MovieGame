import psycopg2
import json

q = """
select t.titleId, t.title, tb.startYear from titles_base tb
inner join titles t
on t.titleId = tb.tconst
where tb.titleType = 'movie' and tb.startYear <> '\\N' and tb.startYear < '2020' and t.region = 'US'
order by tb.startYear desc;
"""

def row_to_dict(tup):
    return {"id": tup[0], "name": tup[1], "year": tup[2]}

conn = psycopg2.connect("dbname=moviegame user=postgres")
cur = conn.cursor()

cur.execute(q)

o = []
for row in cur.fetchall():
    o.append(row)

with open("db/movie_cache.json", "w") as wf:
    json.dump(o, wf)

