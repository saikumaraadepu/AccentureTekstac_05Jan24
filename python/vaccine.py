while True:
    total_count=int(input('Enter the total no of people in the area:\n'))
    if total_count<=0:
        print('Invalid input')
        break
    single_dose=int(input('Single-dose count:\n'))
    if single_dose<0 or single_dose>total_count:
        print('Invalid input')
        break
    double_dose=int(input('Double-dose count:\n'))
    if double_dose<0 or double_dose>total_count:
        print('Invalid input')
        break
    total_dose=single_dose+double_dose
    if total_dose>total_count:
        print('Invalid input')
        break
    vaccine_count=total_count-total_dose
    print('Not vaccinated people count:',vaccine_count)
    percentage='{:.2f}'.format((double_dose/total_count)*100)
    print('Total vaccinated percentage of people:',percentage)
    choice=int(input('Do you want to continue (1) for yes (0) for no:\n'))
    if choice==0:
        break
    elif choice==1:
        continue
    else:
        print('Invalid input')
        break
