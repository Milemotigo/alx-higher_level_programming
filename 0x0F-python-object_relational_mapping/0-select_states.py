#!/usr/bin/env python3
import MySQLdb
import sys


def accessdb(username, password, db_name):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    cursor = db.cursor()
    connect = "SELECT * FROM states ORDER BINARY BY states.id ASC"

    cursor.execute(connect)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    argv = sys.argv[1:]
    username, password, db_name = argv
    accessdb(username, password, db_name)
