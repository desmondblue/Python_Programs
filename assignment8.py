class Employee: 
    
    def from_string(cls,emp_str):
        firstname,lastname,pay = emp_str.split('-')
        return cls(firstname,lastname,pay)
    def __init__(self,first,last,pay):
        self.firstname = first
        self.lastname = last
        self.pay = pay
emp_1_str = 'John-Abraham-50000' 
emp_1 = Employee.from_string(Employee,emp_1_str) #stmt1
print(emp_1.firstname)
print(emp_1.lastname)
print(emp_1.pay)