def operation(mylist):
    mx,sm=0,0
    for i in range(len(mylist)):
        for j in range(len(mylist)):
            if(mylist[i][j]>mx):
                mx=mylist[i][j]
            sm=sm+mylist[i][j]
   
    return mx,sm
    # # print(len(mylist))
    
my_list=[[3,5,6],[7,8,44],[33,1,99]]

value1,value2=operation(my_list)
print(value1," is the Maximum value");
print(value2," is the sum");