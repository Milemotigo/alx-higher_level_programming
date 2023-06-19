#!/usr/bin/python3
'''a script that lists all the cities
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    query = "SELECT s.name, c.name FROM cities c\
            JOIN states s ON c.state_id = s.id\
            ORDER BY s.id ASC, c.id ASC"
    cursor.execute(query)

    rows = cursor.fetchall()

    current_state = None

    for row in rows:
        city, state = row
        print(f"('{city}', '{state}')")

    cursor.close()
    db.close()
