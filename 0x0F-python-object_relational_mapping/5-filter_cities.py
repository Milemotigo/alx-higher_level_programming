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
    query = "SELECT c.name FROM cities c \
            JOIN states s ON c.state_id = s.id \
            WHERE s.name LIKE BINARY %(state_name)s \
            ORDER BY c.id ASC"
    cursor.execute(query, {'state_name': argv[4]})

    rows = cursor.fetchall()

    cities = [row[0] for row in rows]
    city_list = ", ".join(cities)

    print(city_list)

    cursor.close()
    db.close()
