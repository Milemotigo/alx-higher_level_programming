import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user="mysql username",
    passwd="mysql password",
    db="hbtn_0e_0_usa"
)

cursor = db.cursor()
connect = "SELECT * FROM states ORDER BY states.id ASC"

cursor.execute(connect)

results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
db.close()
