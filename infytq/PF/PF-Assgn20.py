#PF-Assgn-20

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    ela = 0 #eligible_loan_amount
    bee= 0 #bank_emi_expected
    ac = str(account_number) #account number to string
    flag = 0
    if len(ac)!=4 or ac[0]!='1':
        print("Invalid account number")
        return 0
    elif account_balance <100000:
        print("Insufficient account balance")
        return 0
    else:
        
        if loan_type =="Car":
            if salary <=25000:
                flag=1
            else:
                ela = 500000
                bee = 36
        elif loan_type =="House":
            if salary <=50000:
                flag = 1
            else:
                ela = 6000000
                bee = 60
        elif loan_type == "Business":
            if salary <=75000:
                flag = 1
            else:
                ela = 7500000
                bee = 84
        else:
            print("Invalid loan type or salary")
            return 0
    if flag ==1:
        print("Invalid loan type or salary")
        return 0
    else:
        if ela<loan_amount_expected or bee<customer_emi_expected:
            print("The customer is not eligible for the loan")
        else:
            print("Account number:", account_number)
            print("The customer can avail the amount of Rs.",ela)
            print("Eligible EMIs :", bee)
            print("Requested loan amount:", loan_amount_expected)
            print("Requested EMI's:",customer_emi_expected)

calculate_loan(2005,300000,255000,"Car",30000,30)
