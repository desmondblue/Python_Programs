'''
Write a python function, remove_duplicates() which accepts a string and removes all duplicate characters from the given string and return it.


Also write the pytest test cases to test the program.

'''
#PF-Assgn-60
def remove_duplicates(value):
    #start writing your code here
    string =''
    for i in value:
        if i not in string:
            string+=i
    return string
print(remove_duplicates("ABCD@^(EFG)%"))
