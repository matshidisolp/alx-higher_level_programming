#!/usr/bin/python3
"""
Module list all states with name starting with N
"""

if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        port=3306,
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset='utf8'
    )
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states\
            WHERE name Like BINARY "N%"\
            ORDER BY id ASC ')
    query = cursor.fetchall()
    for row in query:
        print(row)
    cursor.close()
    db.close()
