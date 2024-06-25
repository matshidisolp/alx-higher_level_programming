#!/usr/bin/python3

"""
Module to connect to a MySQL database and retrieve all from states table.
The script takes three arguments from the command line:
1. MySQL username
2. MySQL password
3. Database name

Usage:
    ./script_name.py <username> <password> <database_name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
