#PF-Assgn-43

def find_smallest_number(num):
    #start writing your code here
    for i in range(1,500):
        list = []
        list.append(i)
        for j in range(1,i):
            if i%j==0:
                list.append(j)
        if len(list) ==num:
            return i    
            break
                

num=16
print("The number of divisors :",num)
try:
    result=find_smallest_number(num)
    print("The smallest number having",num," divisors:",result)
except ValueError as e:
    print("e")
except TypeError as e:
    print("e")
