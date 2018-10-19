import cx_Oracle
con = cx_Oracle.connect("system/therockstar@localhost/xe")
cur = con.cursor()
print("Before update, values for User ID 4 is:")
statement= "SELECT * FROM Users where user_id = 4"
cur.execute(statement)
res = cur.fetchall()
print(res)
cur.execute("UPDATE Users SET user_name = 'lookingforjob@yahoo.com' , user_type = 'Jobseeker' WHERE user_id = 4")
con.commit()
statement= "SELECT * FROM Users where user_id = 4"
cur.execute(statement)
res = cur.fetchall()
print("After update, values for User ID 4 is:","\n",res)
statement = "select password from Users where user_id =1"
cur.execute(statement)
res = cur.fetchall()
print("Before update password for User ID 1 is:",res)
pwd = input("Please enter a new password:")
cur.execute("UPDATE Users SET password = :p1 WHERE user_id = :p2",(pwd,1))
con.commit()
statement ="SELECT password FROM Users where user_id = 1"
cur.execute(statement)
res = cur.fetchall()
print("After update password for User ID 1 is:",res)
