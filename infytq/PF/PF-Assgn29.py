#PF-Assgn-29
def calculate(distance,no_of_passengers):
    
    
    ppl = 70 #Price per litre of fuel 
    mil = 10 #Mileage of the bus in km/litre of fuel 
    ticket = 80 #Price(Rs) per ticket 
    cost = 0
    profit = 0
    cost = (distance/mil)*ppl
    sales = no_of_passengers*ticket
    profit = sales-cost
    if sales <cost:
        return -1
    else:
        return profit



#Provide different values for distance, no_of_passenger and test your program
distance=100
no_of_passengers=10
print(calculate(distance,no_of_passengers))
