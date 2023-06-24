#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access the database and retrieve the states.
    """
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        port=3306,
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}'\
            ORDER BY states.id ASC".format(argv[4])
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
