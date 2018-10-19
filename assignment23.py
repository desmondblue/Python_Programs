class Faculty:
    def addExpertise(self,course):
        self.__coursesExpertise.append(course)
    def __init__(self,name):
        self.__name = name
        self.__coursesExpertise=[]
class Student:
    def enroll(self,course):
        self.__enrolledCourses.append(course)
    def __init__(self,student_id):
        self.__id = student_id
        self.__enrolledCourses=[]
class Course:
    def registerStudent(self,student):
        self.__registeredStudents.append(student)
    def registerExpert(self,faculty):
        self.__expertFaculties.append(faculty)
    def __init__(self,name):
        self.__name=name
        self.__registeredStudents=[]
        self.__expertFaculties=[]
