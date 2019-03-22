#PF-Assgn-34
def find_pairs_of_numbers(num_list,n):
    count = 0
    #Remove pass and write your logic here
    for i in num_list:
        for j in num_list:
            if i ==j:
                continue
            else:
                if i+j == n:
                    count +=1
    count//=2                
    return count

num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))
'''

Sample Input	              |  Expected Output
[1, 2, 7, 4, 5, 6, 0, 3], 6 | 	3
[3, 4, 1, 8, 5, 9, 0, 6], 9	|  4

'''
