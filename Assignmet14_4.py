#Assignment 14 question 4

n0 = 0
n1 = 1 
n2 = input("Enter elements to be displayed")
n2=int(n2)
n3 = 0
print("Fibonacci series : ")
print(n0)
print(n1)
for i in range(n2) :
    n3 = n0 + n1
    print(n3)
    n0=n1
    n1=n3
