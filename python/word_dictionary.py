
##Do not change the code skeleton given.  Write your program in the provided places alone.

def main():
    ### Write your code here
    word_dictionary={}
    while True:
        word=input('Enter the word:\n')
        no_of_meanings=int(input('Enter the no of meanings:\n'))
        if no_of_meanings<=0:
            print('Invalid Input')
            for key,value in word_dictionary.items():
                print(f'{key}:{value}')
            break
        else:
            meanings=[]
            print('Enter the meanings:')
            for i in range(no_of_meanings):
                data=input()
                meanings.append(data)
            word_dictionary[word]=meanings
            choice=int(input('Do you want to add one more elements to the dictionary? If yes, press 1, else press 0:\n'))
            if choice==1:
                continue
            elif choice==0:
                print("Here's the dictionary you've created:")
                for key,value in word_dictionary.items():
                    print(f'{key}:{value}')
                break
            else:
                print('Invalid Input')
                print("Here's the dictionary you've created:")
                for key,value in word_dictionary.items():
                    print(f'{key}:{value}')
                break
    return



if __name__=='__main__':
    main()
    