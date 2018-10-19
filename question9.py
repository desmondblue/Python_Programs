import cx_Oracle
con = cx_Oracle.connect("system/therockstar@localhost/xe")
cur = con.cursor()
try:
    statement = "delete from Incorrect_Table where userid = 2"
    cur.execute(statement)
except cx_Oracle.DatabaseError as xcptn:
    error, = xcptn.args
    print("Error Code:",error.code)
    print("Oracle-Error-Message",error.message)