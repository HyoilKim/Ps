-- 최댓값 구하기 --
select max(DATETIME)
from ANIMAL_INS

-- 최솟값 구하기 --
select min(DATETIME)
from ANIMAL_INS

-- 동물 수 구하기 --
SELECT count(ANIMAL_ID) as count
from ANIMAL_INS

-- 중복 제거하기 --
SELECT count(distinct Name)
FROM ANIMAL_INS