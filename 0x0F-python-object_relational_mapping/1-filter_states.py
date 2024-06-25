#!/usr/bin/python3
"""
Module list all states with name starting with N
"""

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
