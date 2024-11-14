-- 코드를 작성해주세요
SELECT HD.DEPT_ID, DEPT_NAME_EN, ROUND(AVG(SAL)) AS AVG_SAL
FROM HR_DEPARTMENT HD JOIN HR_EMPLOYEES HE ON HD.DEPT_ID = HE.DEPT_ID
GROUP BY DEPT_ID
ORDER BY AVG_SAL DESC