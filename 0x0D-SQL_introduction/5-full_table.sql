--prints the full description of first_table from 
--the database hbtn_0c_0 in MySQL server
SELECT COLUMN_NAME, COLUMN_TYPE
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0'
AND TABLE_NAME = 'first_table';

