subject1=int(input('Enter marks for subject1: \n'))
subject2=int(input('Enter marks for subject2: \n'))
subject3=int(input('Enter marks for subject3: \n'))

if (subject1 or subject2 or subject3)<=0 or (subject1 or subject2 or subject3)>100:
    quit()
cal=lambda s1,s2,s3:round((((s1+s2+s3)/300)*100),1)
percentage=cal(subject1,subject2,subject3)
print(f'Percentage is {percentage}')