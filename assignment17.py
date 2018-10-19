class Employee:
    Salary
    def getSalary(self,payday,lop):        
        pass
class Faculty:
    Remuneration
    def teach(self,course):
        pass
class Visitor:
    Remuneration
    def calculateFees(self,startTime,endTime):
        pass
class clerk(Employee):
    def prepareBalancesheet(self):
        pass
class RegularFaculty(Employee,Faculty):
    def prepareAttendanceReport(self):
        pass
class VisitingFaculty(Faculty,Visitor):
    pass
class Examiner(Visitor):
    def examine(self):
        pass
