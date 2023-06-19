#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    d_base = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], d_base=argv[3])

    cur = d_base.cursor()
    cur.execute("SELECT * FROM states")
    results = cur.fetchall()

    for result in results
        print(results)