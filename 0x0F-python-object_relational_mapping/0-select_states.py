#!/usr/bin/python3
import MySQLdb
import sys


def accessdb(username, password, db_name):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    connect = "SELECT * FROM states ORDER BY states.id ASC"

    cursor.execute(connect)

    rows = cursor.fetchall()

    for row in results:
        print(rows)

    cursor.close()
    db.close()


if __name__ == "__main__":
    argv = sys.argv[1:]
    username, password, db_name = argv
    accessdb(username, password, db_name)
