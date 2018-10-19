class Account:
    def __init__(self, initial_amount):
        self.__balance = initial_amount
    def withdraw(self,amount):
        self.__balance = self.balance - amount
    def deposit(self,amount):
        self.__balance = self.balance + amount 
ac = Account(1000)
ac.balance = 2000 #stmt1
ac.balance = -1000 #stmt2
print(ac.balance) #stmt3
   
