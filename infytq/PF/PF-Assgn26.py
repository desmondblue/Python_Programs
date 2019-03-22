#PF-Assgn-26

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    factor = 0
    #flag =0
    if heads>legs:
        print(error_msg)
        return 0
    if legs/heads ==2:
        chicken_count = heads
        rabbit_count = 0
        
    elif legs/heads==4:
        rabbit_count =heads
        chicken_count =0
        
    else:
        if (legs - 2*heads)//2 == (legs - 2*heads)/2:
            factor = (int)(legs - 2*heads)//2
            rabbit_count =factor
            chicken_count = heads - factor
        else:
            print(error_msg)
            return 0
    print(chicken_count,rabbit_count)
   

#Provide different values for heads and legs and test your program
solve(23,67)
