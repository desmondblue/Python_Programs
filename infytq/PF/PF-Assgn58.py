#PF-Assgn-58
def validate_credit_card_number(card_number):
    #start writing your code here
    temp = str(card_number)
    even =''
    odd = ''
    for i in range(0,len(temp)):
        if i%2!=0:
            odd+=temp[i]
        else:
            even+=temp[i]
    #step 1 A and 1 B
    check_sum =0
    for i in range(0,len(even)):
        pmry = int(even[i])*2
        if pmry >9:
            sum =0
            while(pmry>0):
                r= pmry%10
                sum+=r
                pmry=pmry//10
            pmry = sum
            check_sum+=pmry
        else:
            check_sum +=pmry
    
    #Step 2
    for i in odd:
        check_sum+=int(i)
    
    #Step 3
    if check_sum%10==0:
        return True
    else:
        return False

card_number= 1456734512345696
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")
