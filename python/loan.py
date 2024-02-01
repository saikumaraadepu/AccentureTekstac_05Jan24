import json

def filter_customers(loan_type):
    with open('loan.json')as json_file:
        data=json.load(json_file)
        customers=data['customers']
        count=0
        for customer in customers:
            loans=customer['loans']
            for loan in loans:
                if loan['loan_type'].lower()==loan_type:
                    count+=1
        if count==0:
            print('No customers available')
        else:
            print('Loan Details')
            print('Account_Number\tCustomer_Name\tLoan_Amount')
            for customer in customers:
                loans=customer['loans']
                for loan in loans:
                    if loan['loan_type'].lower()==loan_type:
                        print(customer['Account_Number'],'\t',customer['customer_name'],'\t',loan['loan_amount'])
                        
loan_type=input('Enter the loan type\n')
filter_customers(loan_type)