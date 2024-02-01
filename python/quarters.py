months=('January','February','March','April','May','June','July','August','September','October','November','December')
first_quarter=months[0:3]
second_quarter=months[3:6]
third_quarter=months[6:9]
fourth_quarter=months[9:]
print('Months in expanded form:')
for i in range(len(months)):
    print(months[i])
print('\nThe four quarters are:')
print('\nFirst Quarter:')
for i in range(len(first_quarter)):
    print(first_quarter[i])
print('\nSecond Quarter:')
for i in range(len(second_quarter)):
    print(second_quarter[i])
print('\nThird Quarter:')
for i in range(len(third_quarter)):
    print(third_quarter[i])
print('\nFourth Quarter:')
for i in range(len(fourth_quarter)):
    print(fourth_quarter[i])