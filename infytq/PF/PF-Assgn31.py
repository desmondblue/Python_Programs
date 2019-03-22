#PF-Assgn-31
def check_palindrome(word):
    word= word.lower()
    j=len(word)-1
    b = word[::-1]
    if(word!=b):
           return False
    elif(word==b):
          return True




status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
'''
Write a function, check_palindrome() to check whether the given string is a palindrome or not. The function should return true if it is a palindrome else it should return false.

Note: Initialize the string with various values and test your program. Assume that all the letters in the given string are all of the same case. Example: MAN, civic, WOW etc. 

Also write the pytest test cases to test the program. 
'''
