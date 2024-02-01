
##Do not change the code skeleton given.  Write your program in the provided places alone.

def main():
    ### Write your code here
    subjects=int(input('Enter the no.of subjects:'))
    mark_list=[]
    pass_count,fail_count=0,0
    if subjects<=0:
        print('Invalid no.of subjects')
        quit()
    else:
        print('Enter the marks:')
        for i in range(subjects):
            mark=int(input())
            if mark<0 or mark>100:
                print('Invalid mark')
                quit()
            else:
                mark_list.append(mark)
        for i in range(subjects):
            if mark_list[i]<=50:
                fail_count+=1
            else:
                pass_count+=1
        print('No.of subjects passed:',pass_count)
        print('No.of subjects failed:',fail_count)
        
    return



if __name__=='__main__':
    main()
    