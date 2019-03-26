#PF-Assgn-46

def nearest_palindrome(number):
    #start writitng your code here
    while(True):
        number+=1
        if str(number) ==str(number)[::-1] and len(str(number))>=2:
            return number
    

number=0
print(nearest_palindrome(number))

'''
Write a python function, nearest_palindrome() which accepts a number and returns the nearest palindrome greater than the given number. 
Also write the pytest test cases to test the program.

'''
