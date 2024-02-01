number=int(input('Enter a number\n'))
if number<0:
    print('Factorial does not exist for negative numbers')
else:
    factorial=1
    for i in range(1,number+1):
        factorial=factorial*i
    print('Factorial is',factorial)