import cx_Oracle
con = cx_Oracle.connect("system/therockstar@localhost/xe")
cur = con.cursor()

statement2 = '''create table Employer(
    	CompanyID VARCHAR2(5)PRIMARY KEY ,
	CompanyName VARCHAR2(30),
    EmailId VARCHAR2(20),
    Mobile NUMBER(10),
    City VARCHAR2(20),
    IndustryType VARCHAR2(20),
    FunctionalArea VARCHAR2(20),
    MembershipPlan VARCHAR2(20),
    DateofSignup Date, 
    DateofRenewal Date, 
    RenewalStatus VARCHAR2(20)
    		)'''
cur.execute(statement2)
#delete rows
statement = 'delete from Employer'
cur.execute(statement)
con.commit()
statement = "insert into Employer values('C1000','Infosys Limited', 'jobs@infosys.com',7986579875,'Chennai','IT','Accounting','Yearly','1-Jul-16','30-Jun-17','Active')"
cur.execute(statement)
con.commit()
statement = "insert into Employer values('C1001','Accenture','career@accenture.com',9878776567,'Bangalore','IT','Marketing','Monthly','2-Jun-16','1-Jun-17','Active')"
cur.execute(statement)
con.commit()
statement = "insert into Employer values('C1002','HP', 'openings@hp.com',8789878750,'Mumbai','IT','Marketing','Monthly','12-Jul-16','11-Jul-17','Active')"
cur.execute(statement)
con.commit()
statement = "insert into Employer values('C1003','NewGen', 'jobs@newgen.com',8877643228,'Bangalore','Manufacturing','Marketing','Yearly','2-Sep-16','1-Sep-17','Expired')"
cur.execute(statement)
con.commit()
#Fetch All rows
statement = "select * from Employer"
cur.execute(statement)
res = cur.fetchall()
print(res)
#Count of fetched rows
print("Count of rows :",cur.rowcount)
#Description of all rows
print("Description:",cur.description)
statement = "drop table Employer"
cur.execute(statement)
con.close()
