import MySQLdb
import sys

def accessdb(username, password, data_base)
    d_base = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=data_base  
        
    )

cursor = d_base.cursor()
connect = "SELECT * FROM states ORDER BY states.id ASC"

cursor.execute(connect)

results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
db.close()

argv = sys.argv[1:]
username, password, d_base = argv
accessdb(username, password, db_name)
