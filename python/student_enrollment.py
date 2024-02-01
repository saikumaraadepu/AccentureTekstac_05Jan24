
##Do not change the code skeleton given.  Write your program in the provided places alone.

def main():
    ### Write your code here
    n=int(input('Enter the no of participants details to be created :\n'))
    student_list=[]    
    if n>0:
        for i in range(n):
            student={}
            name=input('Name:\n')
            state=input('State:\n')
            age=int(input('Age:\n'))
            if age<=10 or age>80:
                print('Invalid input')
                continue
            student['Name']=name
            student['State']=state
            student['Age']=age
            student_list.append(student)
        print("Here's the list of participants details:")
        for i in student_list:
            print(i)
        res={}
        for i in student_list:
            if i['State'] not in res.keys():
                res[i['State']]=1
            else:
                res[i['State']]=res[i['State']]+1
        for key,value in res.items():
            print('State:',key,'Count:',value)
    else:
        print('Invalid input')
    return



if __name__=='__main__':
    main()
    