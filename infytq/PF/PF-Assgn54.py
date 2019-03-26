#PF-Assgn-54
def check_anagram(data1,data2):
    flag =0
    if len(data1)!=len(data2):
        return False
    for i in range(0,len(data1)):
        if data1[i].lower()==data2[i].lower():
            return False
        elif data1[i].lower() in data2.lower():
            flag =1
        elif data1[i].lower() not in data2.lower():
            return False
    if flag ==1:
        for i in range(0,len(data1)):
            if data2[i].lower() in data1.lower():
                flag ==1
            else:
                return False
    if flag ==1:
        return True
print(check_anagram("aab","bca"))
