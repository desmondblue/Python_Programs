import cx_Oracle
con = cx_Oracle.connect("system/therockstar@localhost/xe")
cur = con.cursor()
cur.execute('drop table Account')

cur.execute("""create table Account(
            CustomerId   Number Primary Key,
            AccountNo    Varchar2(15),
            AccountType    Varchar2(15) check (AccountType in('Savings','Current','Recurring')),
            Balance    Number 
            )"""
        )

statement = "insert into Account values(:p1,:p2,:p3,:p4)"
cur.executemany(statement,[{'p1':101,'p2':'IBI1001','p3':'Savings','p4':0},{'p1':102,'p2':'IBI1002','p3':'Current','p4':1200},{'p1':103,'p2':'IBI1003','p3':'Savings','p4':6543},{'p1':104,'p2':'IBI1004','p3':'Recurring','p4':7500},{'p1':105,'p2':'IBI1005','p3':'Current','p4':0}])

statement = "select Balance from Account"
cur.execute(statement)
res = cur.fetchall()
max_bal = max(res)
max_bal = max_bal[0]
statement = "select CustomerId, Balance from Account where Balance = :1"
cur.execute(statement,{'1':max_bal})
res = cur.fetchall()
print("Customer with maximum balance has customer id and balance",res)
cur.execute("select Balance from Account where CustomerId = 102")
res = cur.fetchall()
acct_bal = res[0][0]
acct_bal= acct_bal +2000

statement ="update Account set Balance = :up where CustomerId = 102"
cur.execute(statement,{'up':acct_bal})
cur.execute("select Balance from Account where CustomerId = 102")
res = cur.fetchall()
res=res[0][0]
print("Updated Account Balance of Customer with Customer ID 102 is:",res)

statement ="delete from Account where Balance =0"
cur.execute(statement)
cur.execute("select * from Account")
print("Updated table\n",cur.fetchall())

con.close()