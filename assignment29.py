
def Discount(age):
    discount = 0 
    if age >=60 and age <70:
        discount = 15
    elif age >= 70:    
        discount =30
    
    return discount
ages = []
for i in range(6):
    age = input("Enter age")
    ages.append(int(age))
j = 1
for i in ages:    
    print("Test case",j,". Customer Age = ",i,"Discount = ",Discount(i))
    j+=1