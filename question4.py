import cx_Oracle
con = cx_Oracle.connect("system/therockstar@localhost/xe")
cur = con.cursor()
drop_table = 'drop table Vehicle'
cur.execute(drop_table)
cur.execute("""CREATE TABLE Vehicle(
                vehicle_id Number(5) PRIMARY KEY,
                vehicle_name Varchar2(10)
            )""")
counter = 2001            
statement="INSERT INTO Vehicle VALUES(:1,:2)"
cur.executemany(statement,[(counter,'Toyota'),(counter+1,'Maruti'),(counter+2,'Nissan'),(counter+3,'Hyundai')])
con.commit()
counter = 2005
statement="INSERT INTO Vehicle VALUES (:paramID,:paramName)"
cur.executemany(statement,[{'paramID' : counter, 'paramName' : 'Honda'},{'paramID' : counter+1, 'paramName' : 'Volkswagen'}])
con.commit()
cur.execute("SELECT * FROM Vehicle")
res = cur.fetchall()
print(res)

con.close()