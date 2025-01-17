-- 코드를 작성해주세요
WITH T AS (
    SELECT *, PERCENT_RANK() OVER (
        ORDER BY SIZE_OF_COLONY DESC
    ) AS RN
    FROM ECOLI_DATA
)

SELECT ID, 
CASE
WHEN RN<=0.25 THEN 'CRITICAL'
WHEN RN<=0.5 THEN 'HIGH'
WHEN RN<=0.75 THEN 'MEDIUM'
ELSE 'LOW'
END AS COLONY_NAME
FROM T
ORDER BY ID;