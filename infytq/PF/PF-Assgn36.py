#PF-Assgn-36
def create_largest_number(number_list):
    s=''
    x = len(number_list)
    for i in range(0,x):
        
        a = max(number_list)
        s+=str(a)
        del number_list[number_list.index(a)]
    s = int(s)
    return s

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
