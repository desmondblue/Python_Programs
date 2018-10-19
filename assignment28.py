import re
import sys
class udfException(Exception):
    def __init__(self,arg):
        self.x = arg
def isValid(s):
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    return Pattern.match(s)
        
def isAge(age):
    if age<0 or age>=101 :
        return -1
    elif age >0 and age < 101:
        return 1
def isValidEmail(email):      
    if re.match(r"[^@]+@[^@]+\.[^@]+", email)!= None:
        return True
    else:
        return False
        

try:
    s =(input("Enter mobile number:"))
    if(isValid(s)):
        print("Valid Mobile number.")
    else:
        raise udfException("Invalid Mobile number")    
    age = int(input("Enter age"))
    if(isAge(age)==-1):
        raise udfException("Invalid age")
    else:
        print("Valid age.")
    email = input("Enter your email")
    if(isValidEmail(email)):
        print("Valid email.")
    else :
        raise udfException("Invalid email.")
except udfException as e:
    print(e.x)
    
    