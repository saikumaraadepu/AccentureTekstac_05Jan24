def fibonacci(number):
    if number<1 or number>12:
        print('Invalid month')
        quit()
    if number==1:
        return 0
    elif number==2:
        return 1
    else:
        a=0
        b=1
        for i in range(1,number):
            c=a+b
            a=b
            b=c
        return a

month=int(input('Enter the month as numeric value:\n'))
size=fibonacci(month)
print(f'The amoeba size is {size}')
