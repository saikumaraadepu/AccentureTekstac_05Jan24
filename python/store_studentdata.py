no=int(input('Enter number of students: \n'))
file=open('output_data.txt','w')
for i in range(1,no+1):
    print(f'For student {i}')
    name=input('Enter name: \n')
    score=int(input('Enter the score: \n'))
    data_format=f'Name: {name} Score: {score}'
    file.write(f'{data_format}\n')
file.close()
read_file=open('output_data.txt','r')
data=read_file.read()
print('\noutput_data.txt will contain:')
print(data)
read_file.close()