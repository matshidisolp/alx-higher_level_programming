--lists all records of second_table of the db hbtn_0c_0 in MySQL server
--records ordered by score(top first)
SELECT score, name 
FROM second_table 
ORDER BY score DESC;

