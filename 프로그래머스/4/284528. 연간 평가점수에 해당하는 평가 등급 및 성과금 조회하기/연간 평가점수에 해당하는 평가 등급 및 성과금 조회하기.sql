-- 코드를 작성해주세요
SELECT HE.EMP_NO, HE.EMP_NAME, (CASE WHEN AVG(HG.SCORE) >= 96 THEN 'S' 
                                     WHEN AVG(HG.SCORE) >= 90 THEN 'A'
                                     WHEN AVG(HG.SCORE) >= 80 THEN 'B'
                                     ELSE 'C'
                                     END) AS GRADE, 
                                     (HE.SAL * (CASE WHEN AVG(HG.SCORE) >= 96 THEN 0.2 
                                     WHEN AVG(HG.SCORE) >= 90 THEN 0.15
                                     WHEN AVG(HG.SCORE) >= 80 THEN 0.1
                                     ELSE 0
                                     END)) AS BONUS
FROM HR_EMPLOYEES HE JOIN HR_DEPARTMENT HD ON HD.DEPT_ID = HE.DEPT_ID
                     JOIN HR_GRADE HG ON HE.EMP_NO = HG.EMP_NO
GROUP BY HE.EMP_NO
ORDER BY EMP_NO 