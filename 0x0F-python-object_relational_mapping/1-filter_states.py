#!/usr/bin/python3
'''accessing states in ascending order
'''
import MySQLdb
import sys


def accessdb(username, password, db_name):
    '''gain access
    '''
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE state_name LIKE 'N%' ORDER BY states.id ASC")

    rows = cursor.fetchall()

    for row in results:
        print(rows)

    cursor.close()
    db.close()


if __name__ == "__main__":
    argv = sys.argv[1:]
    username, password, db_name = argv
    accessdb(username, password, db_name)
