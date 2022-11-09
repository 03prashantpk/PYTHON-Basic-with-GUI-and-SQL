import mysql.connector as c

db_host = "localhost"
db_port = "3307"
db_user = "root"
db_password = "admin"

conn = c.connect(host = db_host, port = db_port, user = db_user, password = db_password)

cur = conn.cursor()
q1 = "create database k20bn"
cur.execute(q1)