#PF-Assgn-30

def encode(message):
    string = message
    b= []
    b.append(string[0])
    count =1
    c = []
    for i in range(1,len(string)):
        if string[i]!= string[i-1]:
            b.append(string[i])
            c.append(count)
            count = 1    
        elif string[i]==string[i-1]:
            count+=1
        
    c.append(count)
    s =''
    for x,y in zip(b,c):
        s+= str(y)+x
    del(c)
    del(b)
    return(s)
#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCABBB")
print(encoded_message)
