#PF-Assgn-38

def check_double(number):
    n = str(number*2)
    number = str(number)
    flag =0
    for i in n:
        if i in number:
            flag =1
        else:
            flag =0
            break
    if flag ==1:
        return True
    else:
        return False

#Provide different values for number and test your program
print(check_double(245))
