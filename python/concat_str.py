
##Do not change the code skeleton given.  Write your program in the provided places alone.

def concat_string(str1,str2):
    ##Write your code here and return the values
    concat=str1[2:]+str2[2:]
    return (concat,len(concat))#TODO: Return the new string and length of string as two seperate values
    
    

def main():
    ### Write your code here
    string1=input('Enter String1: \n')
    string2=input('Enter String1: \n')
    data=concat_string(string1,string2)
    print(f'The concatenated string: {data[0]}')
    print(f'The length of the new string is :{data[1]}')
    return



if __name__=='__main__':
    main()
    