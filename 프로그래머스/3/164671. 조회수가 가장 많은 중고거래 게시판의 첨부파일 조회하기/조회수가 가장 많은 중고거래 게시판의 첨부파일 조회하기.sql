-- 코드를 입력하세요
SELECT CONCAT('/home/grep/src/',UGB.BOARD_ID,'/',FILE_ID,FILE_NAME, FILE_EXT) AS FILE_PATH
FROM USED_GOODS_BOARD UGB JOIN USED_GOODS_FILE UGF ON UGB.BOARD_ID = UGF.BOARD_ID
WHERE VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
ORDER BY FILE_ID DESC