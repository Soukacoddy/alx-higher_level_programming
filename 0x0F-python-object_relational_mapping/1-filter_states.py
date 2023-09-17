#!/usr/bin/python3
<<<<<<< HEAD
""" Lists all the states from hbtn_0e_0_usa db. """
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
    )
    cursor = db.cursor()
    cursor.execute("""
        SELECT * FROM states
        WHERE name LIKE BINARY 'N%'
        ORDER BY id
    """)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
=======
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8",
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1].startswith("N"):
            print(row)
    cur.close()
    conn.close()
>>>>>>> cc60968cb49ff882fe6beb407b3e4c7dfbcd2cd0
