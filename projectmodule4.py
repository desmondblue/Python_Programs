import cx_Oracle
try:
    from multiprocessing.managers import State
    con = cx_Oracle.connect("system/therockstar@localhost/xe")
    cur = con.cursor()
    

    #estate table
    statement = """ create table rl_estate(
                pid number(10) not null PRIMARY KEY,
                pcat Varchar2(20),
                ploc Varchar2(50),
                ptype Varchar2(20),
                parea Varchar2(50),
                pfur Varchar2(3),
                pvalue number
                      
                )"""
    
    #cur.execute(statement)
    
    #agent table
    
    statement = """ create table rl_agent(
                ag_id number(10) not null PRIMARY KEY,
                ag_name Varchar2(20),
                ag_loc Varchar2(15)
                )"""
    #cur.execute(statement)
    agent_data = [(201,"Rahul Dua","delhi"),(202,"Shankar Chugani","chennai"),(203,"Saurav Mehta","mumbai"),(204,"Sejal Bhatt","kolkata")]
    statement = """insert into rl_agent(ag_id,ag_name,ag_loc) values(:1,:2,:3)  """
    #cur.executemany(statement,agent_data)
    #con.commit()
    
    statement = """create table handlers(
                    ag_id number(10),
                    pid number(10),
                    constraint fk_agent foreign key (ag_id) references rl_agent(ag_id),
                    constraint fk_prop foreign key (pid) references rl_estate(pid)
                    )
                """
    #cur.execute(statement)
    #customer table
    
    statement = """create table rl_customer(
                    cid number(10) not null PRIMARY KEY,
                    cname Varchar2(40),
                    cloc Varchar2(15),
                    cstatus Varchar2(10)
                    )"""
    #cur.execute(statement)
    #owned table
    statement = """ create table owned(
                    pid number(10),
                    cid number(10),
                    constraint fk_estate foreign key (pid) references rl_estate(pid),
                    constraint fk_customer foreign key (cid) references rl_customer(cid)
                )"""
    #cur.execute(statement)
    #BUY/RENT function
    def buy_rent():
        cid = int(input("Enter your customer ID:"))
        pid = int(input("Enter property ID: "))
        agent = getagent(pid)
        print("Please contact our agent",agent,"for further transactions.")
        
        print("Following property has been reserved for you!")
        cur.execute("select * from rl_estate where pid = :p1",{'p1':pid})
        print(cur.fetchall())
        
        statement="insert into owned values(:p1,:p2)"
        cur.execute(statement,{'p1':pid,'p2':cid})
        statement = """update rl_estate set ptype = 'owned' where pid = :p1"""
        cur.execute(statement,{'p1':pid})
        statement = """update rl_customer set cstatus = 'inactive' where cid = :p1"""
        cur.execute(statement,{'p1':cid})
        con.commit()
    #GetAgent function    
    def getagent(pid):
        statement = "select ag_name from rl_agent where ag_id in (select ag_id from handlers where pid =:p1)"
        cur.execute(statement,{'p1':pid}) 
        res = cur.fetchall()
        res = res[0][0]
        return res   
    #CLASS ESTATE
    class rl_estate:
        def __init__(self):
                self.input()
                self.update()
                self.ragent()
                
        def input(self):
                self.pid = int(input("Enter property ID: "))
                self.pcat = input("Enter Category(Apartment,Builder Floor,Villa,Shop,PG): ").lower()
                self.ploc = input("Enter location of the property(Delhi,Mumbai,Chennai,Kolkata):").lower()
                self.ptype = input("Sale / Rent :").lower()
                self.parea = int(input("Enter area of property in sqft: "))
                self.furnished = input("Is furnished?(yes/no): ")
                self.pvalue =0 
                if (self.ptype == "rent" or self.ptype == "Rent") and self.furnished=="yes":
                    self.pvalue  = int((self.parea * 10)) #so as to make monthly rent area multiplied by 10000 divided by 12
                elif (self.ptype == "rent" or self.ptype == "Rent") and self.furnished=="no":
                    self.pvalue  = int((self.parea * 5)) #so as to make monthly rent area multiplied by 6500 divided by 12
                elif (self.ptype == "Sale" or self.ptype == "sale") and self.furnished=="yes":
                    
                        if self.parea > 20000 :
                            self.pvalue = self.parea*9000
                        elif self.parea > 12000 and self.parea <=20000:
                            self.pvalue = self.parea*6500
                        else:
                            self.pvalue = self.parea*4500
                elif (self.ptype == "Sale" or self.ptype == "sale") and self.furnished=="no": 
                    if self.parea > 20000 :
                        self.pvalue = self.parea*5000
                    elif self.parea > 15000 and self.parea <=20000:
                        self.pvalue = self.parea*3000
                    else:
                        self.pvalue = self.parea*2000    
                print("Expected Value of property: INR.%d"%self.pvalue)
        
        def update(self):
            statement = """ insert into rl_estate values (:p1,:p2,:p3,:p4,:p5,:p6,:p7)"""
            cur.execute(statement,{"p1":self.pid,"p2":self.pcat,"p3":self.ploc,"p4":self.ptype,"p5":self.parea,"p6":self.furnished,"p7":self.pvalue})
            con.commit()
            print("Property details added to database!")
        def ragent(self):
            statement = "select ag_id from rl_agent where ag_loc = :p1"
            cur.execute(statement,{'p1':self.ploc})
            self.res = cur.fetchall()
            self.ag_id = self.res[0][0]
            
            statement = """insert into handlers values(:1,:2)"""
            cur.execute(statement,(self.ag_id,self.pid))
            self.ag_fee = self.pvalue / 4
            self.ag_fee = "%.2f"%self.ag_fee
            cur.execute("select ag_name from rl_agent where ag_loc=:p1 ",{'p1':self.ploc})
            res = cur.fetchall()
            res = res[0][0]
            print("Agent :",res,"has been assigned to property ID:",self.pid)
            
        def display(self):
            cur.execute("select * from rl_estate where pid= :p1",{'p1':self.pid}) 
            print(cur.fetchall())  
    #Display property function  
    def viewprop():
        print("1.By Location\n2.By minimum area\n3.By category\n4. By customer's budget\n5.For sale\n6.For rent\n7. View all Properties")
        op = int(input("Enter choice (1-7):"))
        if op == 1:
                loc = input("Enter location (choose from Delhi, Mumbai, Kolkata, Chennai):").lower()
                statement ="""select * from rl_estate where ploc =:p1"""
                cur.execute(statement,{'p1':loc})
                res = cur.fetchall()
                for i in res:
                    print(i)
        elif op ==2:
                sqft = int(input("Enter minimum property area:"))
                statement ="""select * from rl_estate where parea >=:p1"""
                cur.execute(statement,{'p1':sqft})
                res = cur.fetchall()
                for i in res:
                    print(i)
        elif op == 3:
                cat = input("Enter category (choose from Villa,Builder Floor,Apartment,Shop,PG): ").lower()
                statement ="""select * from rl_estate where pcat =:p1"""
                cur.execute(statement,{'p1':cat})
                res = cur.fetchall()
                for i in res:
                    print(i)
        elif op == 4:
                value = int(input("Enter your budget: INR."))
                statement ="""select * from rl_estate where pvalue <=:p1"""
                cur.execute(statement,{'p1':value})
                res = cur.fetchall()
                for i in res:
                    print(i)
        elif op ==5:
                print ("Following properties are for sale:")
                statement = "select * from rl_estate where ptype = 'sale'"
                cur.execute(statement)
                res = cur.fetchall()
                for i in res:
                    print(i)
        elif op ==6:
                print ("Following properties are for rent:")
                statement = "select * from rl_estate where ptype = 'rent'"
                cur.execute(statement)
                res = cur.fetchall()
                for i in res:
                    print(i)
        elif op ==7:
                print ("Following properties:")
                statement = "select * from rl_estate where ptype = 'rent' or ptype = 'sale'"
                cur.execute(statement)
                res = cur.fetchall()
                for i in res:
                    print(i) 
        else:
            print("Incorrect choice.")
        print("Interested in buying or renting any property?")
        xyz = input("Enter yes or no: ")
        if xyz == 'yes':
            buy_rent() 
         
    #CUSTOMER CLASS           
    class rl_customer:
        def __init__(self):
            self.cid = int(input("Enter customer ID: ")) # Customer id
            self.cname = input("Enter customer name: ") #Cusotmer Name
            self.cloc= input("Enter your location (choose from Delhi,Kolkata,Mumbai,Chennai):").lower()
            self.cbudget= int(input("Enter customer budget: ")) #Maximum amount customer willing to spend
            self.ctype = input("looking for buying/ renting?(enter buy / rent):").lower()      
            self.update()   
            self.view_estate()
        def view_estate(self):
            if self.ctype == "buy" :
                statement = """select * from rl_estate where ptype = 'sale' and ploc = :p2 and  pvalue <= :p1"""
                cur.execute(statement,{'p1':self.cbudget,'p2':self.cloc})
                res = cur.fetchall()
                print("Properties that may interest you:")
                for i in res: print(i)
                print("Interested in buying or renting any property?")
                xyz = input("Enter yes or no: ")
                if xyz == 'yes':
                    buy_rent()  
            elif self.ctype == "rent":
                statement = """select * from rl_estate where ptype = 'rent' and pvalue <= :p1 and ploc = :p2"""
                cur.execute(statement,{'p1':self.cbudget,'p2':self.cloc})
                res = cur.fetchall()
                print("Properties that may interest you:")
                for i in res: print(i)
                print("Interested in buying or renting any property?")
                xyz = input("Enter yes or no: ")
                if xyz == 'yes':
                    buy_rent()  
            else:
                print("Incorrect customer details added")
        def update(self):
            statement = """ insert into rl_customer values (:p1,:p2,:p3,:p4)"""
            cur.execute(statement,{"p1":self.cid,"p2":self.cname,"p3":self.cloc,"p4":"active"})
            con.commit()
            print("Customer details added to database!")
    
    ch = 0
    
    while(ch <=3):
            
            print("Menu\n1.Enter Real Estate Details\n2.Enter Customer Details\n3.View Property \n4.Buy or Rent estate\n5.Exit")
            ch = int(input("Enter choice (1-5): "))
            if ch == 1:
                r1 = rl_estate()
            elif ch == 2:
                c1 = rl_customer()
            elif ch == 3:
                viewprop()
               
            elif ch == 4:
                print("Browse our real estate catalogue:")
                viewprop()
            elif ch == 5:
                print("You chose to exit. Thanks for using the software.")
            else:
                raise ValueError
    con.close()
except ValueError as e:
    print("Value Error!",e)
except TypeError as e:
    print("Type Error!",e)
except IOError as e:
    print("IO Error!",e)
except cx_Oracle.DatabaseError as e:
    print("Database Error!",e)