-- 코드를 작성해주세요
SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE (GENOTYPE & 1 > 0 OR GENOTYPE & 4 > 0) AND (GENOTYPE & 2 = 0)