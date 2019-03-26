#PF-Assgn-44


def find_duplicates(list_of_numbers):
    #start writing your code here
    if len(list_of_numbers)!=len(set(list_of_numbers)):
        
        set_list = set(list_of_numbers)
        duplicate_list=[]
        for i in set_list:
            
            count = list_of_numbers.count(i)
            if count>1:
                duplicate_list.append(i)
                
        return duplicate_list
    else:
        b =[]
        return b

list_of_numbers=[0,0,1,23,1,2,3,4,5]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
