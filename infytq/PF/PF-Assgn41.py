#PF-Assgn-41
def find_ten_substring(num_str):
    c =[] #List where substrings will be stored
    for i in range(0,len(num_str)):
        sum = 0
        b='' # empty string to capture substring
        while(i<=len(num_str)-1):
            sum+=int(num_str[i])
            b+=num_str[i]
            i+=1
            if sum==10:
                c.append(b)
                
    if c:
        return c
    else:
        return "invalid"            
        

num_str="3523014"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
