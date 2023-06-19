#!/usr/bin/python3
'''script that lists all states
'''

import MySQLdb
import sys


if __name__ == "__main__":
    def accessdb(username, password, db_name):
        '''connection
        '''
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            charset="utf8"
        )

        curs = db.cursor()
        connect = "SELECT * FROM states ORDER BY states.id ASC"

        curs.execute(connect)

        results = curs.fetchall()

        for row in results:
            print(row)

        cursor.close()
        db.close()



        argv = sys.argv[1:]
        username, password, db_name = argv
        accessdb(username, password, db_name)
