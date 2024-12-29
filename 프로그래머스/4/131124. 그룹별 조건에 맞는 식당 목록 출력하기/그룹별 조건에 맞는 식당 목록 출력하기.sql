-- 코드를 입력하세요
SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE,'%Y-%m-%d')
FROM MEMBER_PROFILE MP JOIN REST_REVIEW RR ON MP.MEMBER_ID = RR.MEMBER_ID
WHERE MP.MEMBER_ID IN (
                SELECT MEMBER_ID 
                FROM REST_REVIEW
                GROUP BY MEMBER_ID
                HAVING COUNT(*) = (
                            SELECT MAX(TOTAL)
                            FROM (SELECT MEMBER_ID, COUNT(*) AS TOTAL
                            FROM REST_REVIEW
                            GROUP BY MEMBER_ID) REVIEW_COUNT))
ORDER BY REVIEW_DATE, REVIEW_TEXT
