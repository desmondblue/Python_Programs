import cx_Oracle
con = cx_Oracle.connect("system/therockstar@localhost/xe")
cur = con.cursor()
drop_table = "drop table Users"
cur.execute(drop_table)
cur.execute("""CREATE TABLE Users(
user_id Number(10) PRIMARY KEY,
user_name Varchar2(30) NOT NULL,
password Varchar2(20) NOT NULL,
user_type Varchar2(20) CHECK (user_type IN ('Employer', 'Jobseeker'))
)""")
cur.execute("INSERT INTO Users VALUES (1,'jobs@infosys.com','jobs@infosys','Employer')")
u_id = 2
u_name = 'careers@accenture.com'
pwd = 'Acc1'
u_type = 'Employer'
cur.execute("INSERT INTO Users VALUES(:p1,:p2,:p3,:p4)",(u_id,u_name,pwd,u_type))
u_id1 = 3
u_name1 = 'rahulitsme@gmail.com'
pwd1 = 'rahulindia93'
u_type1 = 'Jobseeker'
cur.execute("INSERT INTO Users VALUES(:param1,:param2,:param3,:param4)",{'param1' : u_id1, 'param2' : u_name1, 'param3' : pwd1, 'param4' : u_type1})
uid = int(input("Please insert the user ID:"))
uname = input("Please insert the user name:")
upwd = input("Please insert the password:")
utype = input("Please insert the user type:")
cur.execute("insert into Users values(:p5,:p6,:p7,:p8)",{'p5':uid,'p6':uname,'p7':upwd,'p8':utype})
con.commit()
cur.execute("SELECT * FROM Users")
res = cur.fetchall()
print(res)
con.close()
