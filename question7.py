import cx_Oracle
con = cx_Oracle.connect("system/therockstar@localhost/xe")
cur = con.cursor()

statement = "select * from Users"
cur.execute(statement)
res=cur.fetchall()
print("Pre-Deletion Users Table:\n",res)
cur.execute("delete from Users where user_id = 1")
statement = "select * from Users"
cur.execute(statement)
res=cur.fetchall()
print("Post-Deletion Users Table:\n",res)
statement = "select * from Vehicle"
cur.execute(statement)
res=cur.fetchall()
print("Pre-Deletion Vehicle Table:\n",res)
v_id = int(input("Enter Vehicle Id for the record to be deleted:"))
statement ="delete from Vehicle where vehicle_id = :p1"
cur.execute(statement,{'p1':v_id})
statement = "select * from Vehicle"
cur.execute(statement)
res=cur.fetchall()
print("Post-Deletion Vehicle Table:\n",res)
con.close()
           
            