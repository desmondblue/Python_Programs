'''
Consider sample data as follows: sample_data=range(1,11)
Create two functions: odd() and even()
The function even() returns a list of all the even numbers from sample_data
The function odd() returns a list of all the odd numbers from sample_data
Create a function sum_of_numbers() which will accept the sample data and/or a function.
If a function is not passed, the sum_of_numbers() should return the sum of all the numbers from sample_data
If a function is passed, the sum_of_numbers() should return the sum of numbers returned from the function passed.
'''
    #PF-Assgn-52
    

def sum_of_numbers(list_of_num,filter_func=None):
    sum =0
    if filter_func!=None:
        for i in filter_func:
            sum+=i
    else:
        for i in list_of_num:
            sum+=i
    return sum
def even(data):
    beta=[]
    for i in data:
        if i%2==0:
            beta.append(i)
    return beta
def odd(data):
    beta=[]
    for i in data:
        if i%2!=0:
            beta.append(i)
    return beta

sample_data = range(1,11)

print(sum_of_numbers(sample_data,even(sample_data)))
