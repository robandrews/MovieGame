import os
from flask import Flask
from flask import request, send_from_directory
from flask_cors import CORS, cross_origin

import psycopg2
import json

movies_for_actor_template = """
select tb.primaryTitle, n.primaryName, t.tconst from titles_base tb
inner join titles_principals t
on tb.tconst = t.tconst
inner join names n
on t.nconst = n.nconst
where n.nconst = '{}'
and ((category like '%actor%') or (category like '%actress%'));
"""

actors_from_movie_template = """
select * from titles_principals t
inner join names n
on t.nconst = n.nconst
where tconst = '{}'
and ((category like '%actor%') or (category like '%actress%'));
"""

actors_from_movie_template = """
select * from titles_principals t
inner join names n
on t.nconst = n.nconst
where tconst = '{}' and
category in ('actor', 'actress')
order by t.ordering asc;
"""

actor_in_movie_template = """
select '{actor_id}' in
(
    select n.nconst from titles_principals t
    inner join names n
    on t.nconst = n.nconst
    where tconst = '{movie_id}'
    and ((category like '%actor%') or (category like '%actress%'))
);
"""

conn = psycopg2.connect("dbname=moviegame user=postgres")

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return send_from_directory(os.path.join("/".join(os.getcwd().split("/")[:-1]), "web"), "index.html")

@app.route('/movies/<movie_id>')
def movies(movie_id):
    cur = conn.cursor()
    q = "SELECT * FROM titles_base tb inner join titles t on t.titleid=tb.tconst where tb.tconst = '{}'".format(movie_id)
    cur.execute(q)
    colnames = [desc[0] for desc in cur.description]
    res = cur.fetchall()
    return json.dumps(dict(zip(colnames, res)))

@app.route('/actors-from-movie/<movie_id>')
def actors_from_movie(movie_id):
    cur = conn.cursor()
    q = actors_from_movie_template.format(movie_id)
    cur.execute(q)
    res = cur.fetchall()
    return json.dumps(res)

@app.route('/movies-for-actor/<actor_id>')
def movies_for_actor(actor_id):
    q = movies_for_actor_template.format(actor_id)
    cur = conn.cursor()
    cur.execute(q)
    res = cur.fetchall()
    return json.dumps(res)

# Test
# http://localhost:5000/actor-in-movie?actorId=nm0886733&movieId=tt0654803
@app.route('/actor-in-movie')
def actor_in_movie():
    actor_id = request.args.get('actorId')
    movie_id = request.args.get('movieId')
    q = actor_in_movie_template.format(actor_id=actor_id, movie_id=movie_id)
    cur = conn.cursor()
    cur.execute(q)
    res = cur.fetchall()
    return json.dumps(res)
