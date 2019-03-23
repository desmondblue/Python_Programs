#PF-Assgn-42
def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    
    return factors

def is_prime(num, i):
    #Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
    if(i==1):
        return True
    elif(num%i==0):
        return False;
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    dummy_list =[]
    for i in list_of_factors:
        if is_prime(i, i//2):
            dummy_list.append(i)
        else:
            continue   
    value = max(dummy_list)
    return value
    
def find_f(num):
    list = find_factors(num)
    value = find_largest_prime_factor(list)
    return value
def find_g(num):
    #Accepts the number and returns the sum of the largest prime factors of the 9 consecutive numbers starting from the given number
    sum =0
    for i in range(num,num+9):
        a = find_f(i)
        sum+=a
    return sum
#Note: Invoke function(s) from other function(s), wherever applicable.

print(find_g(10))
