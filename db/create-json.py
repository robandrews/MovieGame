import psycopg2
import json

q = """
select t.title
from titles_ratings tr 
inner join titles_base tb 
on tr.tconst=tb.tconst
inner join titles t
on t.titleId = tb.tconst
where tb.titleType = 'movie' and tb.startYear <> '\\N' and tb.startYear < '2020' and t.region IN ('US', '\\N')
    AND t.types = 'original' AND tr.numVotes > 20000
order by tr.numVotes desc
limit 20000;
"""

def row_to_dict(tup):
    return {"id": tup[0], "name": tup[1], "year": tup[2]}

conn = psycopg2.connect("dbname=moviegame user=postgres")
cur = conn.cursor()

cur.execute(q)

o = []
for row in cur.fetchall():
    # o.append(row)
    o.extend(row)

with open("data/movie_cache.json", "w") as wf:
    json.dump(o, wf)

