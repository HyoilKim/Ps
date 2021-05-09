-- 1. 하나의 col으로 만듦
-- 2. col 값으로 grouping
-- 3. 각 group 갯수 세기
SELECT id, COUNT(id) as COUNT
FROM (
    SELECT id1 AS id FROM friends
    UNION ALL
    SELECT id2 from friends) as _
GROUP BY id
ORDER BY id