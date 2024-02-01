n1,n2=map(int,input('Enter the starting and ending numbers:\n').split(" "))
if n1<0 or n2<0:
    print('Starting and ending numbers must be greater than or equal to zero')
    quit()
else:
    if n1>n2:
        print('Invalid input!! Ending number should be greater than starting number')
        quit()
    else:
        print(f'Armstrong numbers between {n1} and {n2} are:\n')
        count=0
        for i in range(n1,n2+1):
            armstrong_num=0
            n=i
            while n!=0:
                ld=n%10
                armstrong_num+=(ld**3)
                n//=10
            if i==armstrong_num:
                print(armstrong_num,'\n')
                count+=1
        if count==0:
            print('There is no Armstrong number between these numbers')
            
            