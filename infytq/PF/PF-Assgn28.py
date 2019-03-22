#PF-Assgn-28

def find_max(num1, num2):
    max_num=-1
    
    if num1>=num2:
        return -1
    list = []
    for i in range(num1,num2+1):
        sum = 0
        count = 0
        temp =i
        
        while temp >0:
            b = temp%10
            sum+=b
            temp= temp//10
            count+=1
        
        if (sum%3==0) and (i%5==0) and (count ==2):
            list.append(i)
        else:
            continue
    if len(list)!= 0:
        max_num = max(list)
        return max_num
    else:
        return -1

#Provide different values for num1 and num2 and test your program.
max_num=find_max(2,14)
print(max_num)
