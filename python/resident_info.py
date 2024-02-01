no_of_residents=int(input('\nNo of Residents :\n'))
residents_list=[]
if no_of_residents<=0:
    print('Invalid')
    quit()
for i in range(no_of_residents):
    print(f'Resident {str(i+1)}:')
    name=input('Name :\n')
    age=int(input('Age :\n'))
    if age<21 or age>58:
        print('Invalid')
        quit()
    designation=input('Designation :\n')
    band=input('Band :\n')
    if band not in ('A','B','C','D'):
        print('Invalid')
        quit()
    resident=(name,age,designation,band)
    residents_list.insert(i,resident)
print("('NAME','AGE','DESIGNATION','BAND')")
for i in residents_list:
    print(i)
band_interest=input('Enter your band of interest:\n')
if band_interest not in ('A','B','C','D'):
    print('Invalid')
    quit()
else:
    band_count=0
    print("('NAME','AGE','DESIGNATION','BAND')")
    for i in residents_list:
        if band_interest in i:
            print(i)
            band_count+=1
    if band_count==0:
        print('No resident under this band')