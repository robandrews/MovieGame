-- SELECT title
-- FROM pgweb
-- WHERE to_tsvector('english', body) @@ to_tsquery('english', 'friend');

-- 1. convert column from the table to_tsvector
-- 2. use @@ for the comparison
-- 3. use to_tsquery to pass in the input query
-- Note: english is the default for both - you can omit those.

-- SELECT title
-- FROM pgweb
-- WHERE to_tsvector(body) @@ to_tsquery('friend');

select * from titles_base tb
inner join titles t
on t.titleId = tb.tconst
where tb.titleType = 'movie' and tb.startYear <> '\N' and tb.startYear < '2019' and t.region = 'US'
order by tb.startYear desc limit 50;


select count(*) from titles_base tb
inner join titles t
on t.titleId = tb.tconst
where tb.titleType = 'movie' and tb.startYear <> '\N' and tb.startYear < '2019' and t.region = 'US';
-- => 157258

-- get movie list to cache
select t.titleId, t.title, tb.startYear from titles_base tb
inner join titles t
on t.titleId = tb.tconst
where tb.titleType = 'movie' and tb.startYear <> '\N' and tb.startYear < '2020' and t.region = 'US'
order by tb.startYear desc;


-- find actors from movie
select * from titles_principals t
inner join names n
on t.nconst = n.nconst
where tconst = 'tt0111161'
and category in ('actor', 'actress');


-- find movies from actor
select tb.primaryTitle, n.primaryName, t.tconst from titles_base tb
inner join titles_principals t
on tb.tconst = t.tconst
inner join names n
on t.nconst = n.nconst
where n.nconst = 'nm0000151'
and category in ('actor', 'actress');