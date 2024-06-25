#!/usr/bin/python3i

"""
Module to connect to a MySQL database and retrieve all from states table.
The script takes three arguments from the command line:
 1. MySQL username
 2. MySQL password
 3. Database name

 Usage:
 ./script_name.py <username> <password> <database_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cur = db.cursor()

    query = (
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' "
        "ORDER BY id ASC"
    )
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
