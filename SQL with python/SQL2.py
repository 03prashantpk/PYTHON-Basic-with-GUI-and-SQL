import mysql.connector as c
import config

# The connection has been established on config.py file
db_conn = config.conn
cur = db_conn.cursor()

#sql = "create table batter (Name varchar(50), Role varchar (50), Runs varchar(50), Centuries varchar(50))"
# sql = "insert into batter values(%s, %s, %s, %s)"
# val = [("ABC", "Opener", 5000, 8),
#        ("Sachin", "Opener", 15000, 100),
#        ("GHI", "Middle Order", 9000, 10)]


#sql = "create table captain2 (Name varchar (50), Team int(10), Matches varchar (3), Wins varchar (3))"
# sql = "insert into captain values(%s, %s, %s, %s)"
# val = [("ABC", "Domestic", 540, 100),
#         ("Sachin", "Global", 120, 100),
#         ("GHI", "Domestic", 90, 10),
#         ("Bot1", "Domestic", 99, 12),
#         ("Bot2", "Global", 80, 80)]

sql = "Update captain SET Matches = 1 WHERE Name = Sachin" 

cur.execute(sql)

#cur.executemany(sql,val)

#db_conn.commit()

print(cur.rowcount, "record inserted.\n")
for x in cur:
    print(x,"\n")