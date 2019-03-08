#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    vc = 120 # veg combo
    nc = 150 #non veg combo
    d = distance_in_kms
    dcost = 0
    if d<=3:
        dcost=0
    elif d<=6 and d>3:
        d-=3
        dcost = d*3
    elif d>6:
        d-=6
        dcost += 9 + d*6
        
    if food_type == 'N':
        bill_amount+= nc*quantity_ordered+dcost
    elif food_type == 'V':
        bill_amount+= vc*quantity_ordered+dcost
    else:
         print("Incorrect food type")
    #write your logic here
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)
