#PF-Assgn-20

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    ela = 0 #eligible_loan_amount
    bee= 0 #bank_emi_expected
    ac = str(account_number) #account number to string
    if len(ac)!=4 or ac[0]!='1':
        print("Invalid account number")
    elif account_balance <100000:
        print("Insufficient account balance")
    else:
        flag = 0
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
                ela = 600000
                bee = 60
        elif loan_type == "Business":
            if salary <=75000:
                flag = 1
            else:
                ela = 750000
                bee = 84
        else:
            print("Invalid loan type or salary")
    if flag ==1:
        print("Invalid loan type or salary")
    else:
        if ela<loan_amount_expected or bee<customer_emi_expected:
            print("The customer is not eligible for the loan")
        else:
            print("Account number:", account_number)
            print("The customer can avail the amount of Rs.",ela)
            print("Eligible EMIs :", bee)
            print("Requested loan amount:", loan_amount_expected)
            print("Requested EMI's:",customer_emi_expected)

calculate_loan(1001,40000,250000,"Car",300000,30)
