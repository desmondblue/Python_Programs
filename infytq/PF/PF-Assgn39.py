#PF-Assgn-39
#This verification is based on string match.     

#Global variables
menu= ('Veg Roll', 'Noodles', 'Fried Rice' , 'Soup')    
quantity_available=[2,200,3,0]

def place_order(*item_tuple):
    for i in range(0,len(item_tuple),2):
        if item_tuple[i] not in menu:
            print(item_tuple[i]+" is not available")
        else:
            pos =menu.index(item_tuple[i])
            if check_quantity_available(pos, item_tuple[i+1]):
                print (item_tuple[i]+" is available")
            else:
                print(item_tuple[i]+" stock is over")

def check_quantity_available(index,quantity_requested):
    if quantity_requested<=quantity_available[index]:
        return True
    else:
        return False
    #Remove pass and write your logic here to return an appropriate boolean value.


#Provide different values for items ordered and test your program

place_order("Fried Rice",2,'Soup',1)
