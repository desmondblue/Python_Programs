 #PF-Assgn-37

#Global variables
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    sum =0
    for i in chocolates_received:
        sum+=i
    return sum
def reward_child(child_id_rewarded,extra_chocolates):
    if extra_chocolates <1:
        print("Extra chocolates is less than 1")
        return 0
    elif child_id_rewarded not in child_id:
        print("Child id is invalid")
        return 0
    else:
        pos = child_id.index(child_id_rewarded)
        chocolates_received[pos]+=extra_chocolates
        
    print(chocolates_received)    
   
    

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    
    


print(calculate_total_chocolates())
#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(46,2)
