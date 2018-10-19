import cx_Oracle
con = cx_Oracle.connect("system/therockstar@localhost/xe")
cur = con.cursor()
cur.execute(""" create table product(
            productid Varchar2(4) Primary Key,
            type    Varchar2(15),
            price    Number,
            quantity    Number
           ) 
            """)
try:
    cur.execute("insert into product values('P106','Jams',150)")
except cx_Oracle.DatabaseError as excpt:
    error, = excpt.args
    print("Error!\nError Code:",error.code)
    print("Error Message",error.message)

con.close()