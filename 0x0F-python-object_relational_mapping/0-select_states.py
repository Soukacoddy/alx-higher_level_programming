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
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
=======
"""
Lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
    states = cur.fetchall()

    for state in states:
        print(state)
>>>>>>> 0dfef8e8acaf36be006ae3219f444ed943db9097
