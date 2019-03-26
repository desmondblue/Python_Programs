#PF-Assgn-48

def find_correct(word_dict):
    #start writing your code here
    correct = 0
    almost = 0
    wrong =0
    for key,value in word_dict.items():
        if key == value:
            correct+=1
        elif len(key) == len(value):
            
            count = 0
            for i in range(0,len(key)):
                if key[i]!=value[i]:
                    count +=1
            
            if count<=2:
                almost+=1
            else:
                wrong+=1
        else:

            wrong+=1
    list =[correct,almost,wrong]
    return list

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))
