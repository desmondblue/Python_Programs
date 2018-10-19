#Assignment 20

n0 = 0
n1 = 1 
n2 = input("Enter the number n: ")
n2=int(n2)
n3 = 0
my_list = [0,1]
j=2
print("Fibonacci series upto:",n2," elements.")
for i in range(n2) :
    n3 = n0 + n1
    my_list.append(n3)
    n0=n1
    n1=n3
    j = j+1
print(my_list)
