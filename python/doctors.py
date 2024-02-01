##Do not change the code skeleton given.  Write your program in the provided places alone.

def main():
    ### Write your code here
    n1=int(input('\n'))
    if n1<=0:
        print('Invalid list size')
        quit()
    id1=[]
    for i in range(n1):
        data=int(input('\n'))
        if data<=0:
            print('Invalid Id')
            quit()
        id1.append(data)
    n2=int(input('\n'))
    if n2<=0:
        print('Invalid list size')
        quit()
    id2=[]
    for i in range(n2):
        data=int(input('\n'))
        if data<=0:
            print('Invalid Id')
            quit()
        id2.append(data)
    not_working_ids=[]
    for i in id1:
        if i not in id2:
            not_working_ids.append(i)
    print("Not Working Doctors' IDs are:")
    for i in not_working_ids:
        print(i,end=' ')
    return



if __name__=='__main__':
    main()