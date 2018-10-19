class Employee:
	def __init__(self,first,last,pay):
		self.firstname = first
		self.lastname  = last
		self.pay = pay
		self.email= first+'.'+last+'@company.com'


emp1 = Employee("Mohandas","Gandhi",50000)

print(emp1.email)