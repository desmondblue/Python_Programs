'''
ARS Gems Store sells different varieties of gems to its customers.

Write a Python program to calculate the bill amount to be paid by a customer based on the list of gems and quantity purchased. Any purchase with a total bill amount above Rs.30000 is entitled for 5% discount. If any gem required by the customer is not available in the store, then consider total bill amount to be -1.

Assume that quantity required by the customer for any gem will always be greater than 0.

Perform case-sensitive comparison wherever applicable.

'''
#PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    #Write your logic here
    for x in reqd_gems:
    
    	if x in gems_list:
    		continue
    	else:
    		return -1
    		break
    for x,y in zip(reqd_gems,reqd_quantity):
    	pos = gems_list.index(x)
    	z = price_list[pos]
    	bill_amount += y*z		
    if bill_amount >30000:
    	bill_amount -= bill_amount*0.05   	
    return bill_amount

#List of gems available in the store
gems_list =['Amber', 'Aquamarine', 'Opal', 'Topaz']	

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[4392, 1342, 8734, 6421]
#List of gems required by the customer
reqd_gems=['Amber', 'Opal', 'Topaz']

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[2, 1, 3]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)
