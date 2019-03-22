#PF-Assgn-35


#Global variable
list_of_marks=(24,24,24,24,24,24,24,24,24,25)
avg =0
for i in list_of_marks:
    avg+=i
total_students = len(list_of_marks)
avg //=total_students
def find_more_than_average():
    count =0
    for i in list_of_marks:
        if i >avg:
            count+=1
    count = (count/len(list_of_marks))*100
    return count
def sort_marks():
    l = list(list_of_marks)
    return sorted(l)

    #Remove pass and write your logic here

def generate_frequency():
    l = list(list_of_marks)
    b= []
    for i in range(0,26):
        count =l.count(i)
        b.append(count)
    return b

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
