class Employee:
	def __init__(self,first,last,pay):
		self.firstname = first
		self.lastname  = last
		self.pay = pay
		self.email= first+'.'+last+'@company.com'
	def getEmail(object):
		return object.email
	def getFullName(self):
		self.fullname = self.firstname + self.lastname
		return self.fullname
	def getPay(object):
		return object.pay
	
emp1 = Employee("Mohandas","Gandhi",50000)

print(emp1.getFullName())
print(emp1.getPay())
print(emp1.getEmail())