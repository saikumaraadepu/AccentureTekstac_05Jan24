##Do not change the code skeleton given.  Write your program in the provided places alone.

def main():
    ### Write your code here
    def find_luck(num):
        sm=0
        while num!=0:
            temp=num%10
            sm+=temp
            num//=10
        if sm%2==0:
            return 1
        else:
            return 0
    number=int(input('Enter the Number:\n'))
    luck=0
    if number<=0:
        print('Invalid Number')
        quit()
    else:
        luck=find_luck(number)
    if luck==1:
        print(f'{number} is lucky')
    else:
        print(f'{number} is not lucky')
    
    
    
    return



if __name__=='__main__':
    main()
    