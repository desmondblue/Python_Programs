#PF-Assgn-33

def find_common_characters(msg1,msg2):
    s =''

    for i in msg2:
        if i in msg1:
            s+=i.strip()
    if not s:
        return -1
    else:
        return s
            

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"

common_characters=find_common_characters(msg1,msg2)
print(common_characters)
