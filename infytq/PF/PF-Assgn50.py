#PF-Assgn-50

def sms_encoding(data):
    #start writing your code here
    list = data.split(" ")
    for i in range(0,len(list)):
        flag =0
        text =''
        for j in list[i]:
            j=j.lower()
            if j not in 'aeiou':
                flag =1
                break
        if flag ==1:  
            for j in list[i]:
                if j.lower() not in 'aeiou':
                    text+=j
            list[i]= text
    data = ' '.join(list)
    return data     

data="GOOD DAYS AND BAD BOYS"
print(sms_encoding(data))
