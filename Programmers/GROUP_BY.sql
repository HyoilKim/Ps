-- 고양이와 개는 몇 마리 있을까 --
SELECT ANIMAL_TYPE, count(ANIMAL_TYPE) as count
from ANIMAL_INS
group by ANIMAL_TYPE
order by ANIMAL_TYPE

-- 동명 동물 수 찾기 --
SELECT * 
FROM (SELECT NAME, COUNT(NAME) as 'COUNT'
      FROM ANIMAL_INS 
      GROUP BY NAME) as _
WHERE COUNT > 1
ORDER BY NAME

SELECT NAME, count(NAME) as 'count'
from ANIMAL_INS
group by NAME
having count >= 2
order by NAME

-- 입양 시각 구하기(1) --
SELECT HOUR, COUNT(HOUR)
FROM (SELECT hour(DATETIME) as HOUR
      FROM ANIMAL_OUTS) as _
GROUP BY HOUR
HAVING HOUR >= 9 and HOUR < 20
ORDER BY HOUR

SELECT HOUR(DATETIME) as HOUR, COUNT(HOUR(DATETIME))
FROM ANIMAL_OUTS
GROUP BY HOUR HAVING HOUR BETWEEN 9 AND 19
ORDER BY HOUR

-- 입양 시각 구하기(2) -- 
WITH RECURSIVE CTE as (
    SELECT 0 as HOUR
    UNION ALL
    SELECT HOUR+1 FROM CTE
    WHERE HOUR < 23
) 

SELECT      CTE.HOUR, COUNT(ANI.ANIMAL_ID)
FROM        CTE
LEFT JOIN   ANIMAL_OUTS AS ANI
ON          CTE.HOUR = HOUR(ANI.DATETIME)
GROUP BY    CTE.HOUR

SELECT HOUR, coalesce(COUNT, 0)
FROM CTE
LEFT JOIN (SELECT HOUR(datetime) AS _HOUR, COUNT(*) as COUNT
           FROM ANIMAL_OUTS
           group by HOUR(datetime)) as ANI
ON CTE.HOUR = ANI._HOUR