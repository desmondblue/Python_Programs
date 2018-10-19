
class Department:
    department = []
    regularFaculties= []
    def __init__(self,name):
        self.deptName = name  
        self.department.append(name)   
    def getDeptName(self):
        return self.deptName
class Employee:
    employee = []
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
        self.employee.append(name)
        self.empID = self.employee.index(name) + 1
    def addEmp(self,name):
        self.employee.append(name)
    def getDesignation(self):
        return self.designation
    def __str__(self):
        a = str(self.empID) +'.'+self.name+'('+self.designation+')'
        return a
    def setDesignation(self,designation):
        self.designation=designation
class RegularFaculty(Employee,Department):
    def __init__(self,name,Dept,designation):
        Employee.__init__(self, name, designation)
        self.dept = Dept.getDeptName()
        self.regularFaculties.append(name)
       
    def __str__(self):
        a = Employee.__str__(self) + '['+self.dept+']'
        return a
    def teach(self,course):
        print(self.name,"teaches",course.display())
    
class Course:
    def __init__(self,name):
        self.courseName = name
    def display(self):
        return self.courseName
class Visitor:
    visitor = []
    def __init__(self,name):
        self.name = name
        self.visitor.append(name)
        self.visitorID = self.visitor.index(name)+1 
    def display(self):
        print ("Visitor for the event",self.name)       
    
class Institution(Department,Employee,Visitor):
    departments =[]
    employees =[]
    def __init__(self,regName):
        self.registeredNamed = regName
    def addDepartment(self,Dept):
        DeptName =Dept.getDeptName()
        self.department.append(DeptName)
        print(DeptName,"department is added.")
        
    def event(self,v1):
        v1.display()
    def recruit(self,empy):
        temp = empy.getDesignation()
        self.employees.append(temp)
        print("recruited:",temp)
d1 = Department("Computer")
e1 = Employee("John","Clerk")
print(e1)
e2 = RegularFaculty("Jack",d1,"Professor")
print(e2)
v1 = Visitor("Bill gates")
inst = Institution("Institute of Technology")
inst.addDepartment(d1)
inst.event(v1)
inst.recruit(e2)
c = Course("Database")
e2.teach(c)