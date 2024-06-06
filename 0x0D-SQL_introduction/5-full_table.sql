-- Prints the full description of the table 
-- first_table from the database hbtn_0c_0
SELECT CONCAT(
    'first_table',
    'CREATE TABLE `first_table` (',
    '`id` int NOT NULL AUTO_INCREMENT,',
    '`name` varchar(128) DEFAULT NULL,',
    '`c` char(1) DEFAULT NULL,',
    '`created_at` date DEFAULT NULL,',
    'PRIMARY KEY (`id`)',
    ') ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci'
) AS full_description;
