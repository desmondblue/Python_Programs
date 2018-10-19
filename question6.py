import cx_Oracle
con = cx_Oracle.connect("system/therockstar@localhost/xe")
cur = con.cursor()

statement = "select * from Vehicle"
cur.execute(statement)
res = cur.fetchall()
print("Pre-Update Vehicle Table:\n",res)
count = 2001
for i in range(1001,1007) :
    statement = "update Vehicle set vehicle_id =:p1 where vehicle_id =:p2"
    cur.execute(statement,(i,count))
    count += 1
cur.execute("update Vehicle set vehicle_name = 'Mahindra' where vehicle_id = 1003")
con.commit()
statement = "select * from Vehicle"
cur.execute(statement)
res = cur.fetchall()

print("Post-Update Vehicle Table:\n",res)
con.close()