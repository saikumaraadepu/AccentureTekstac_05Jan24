no_of_courses=int(input('Enter the number of courses:\n'))
subjects,marks=[],[]
if no_of_courses<1:
    print('Invalid no. of courses')
    quit()
else:
    for i in range(no_of_courses):
        print('Enter the name of the subject and marks respectively:')
        data1=input('\n')
        data2=int(input('\n'))
        if data2<0 or data2>100:
            print('Invalid mark')
            quit()
        else:
            subjects.append(data1)
            marks.append(data2)
    print('The courses you have cleared are:')
    for i in range(no_of_courses):
        if marks[i]>=80:
            print(f'{subjects[i]} {marks[i]}')