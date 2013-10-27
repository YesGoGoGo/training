-- Question 2
-- Find all years that have a movie that received a rating of 4 or 5, and sort them in increasing order.

select m.year
from movie m, rating r
where r.stars in (4, 5)
group by year
order by year

