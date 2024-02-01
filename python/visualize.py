##Do not change the code skeleton given.  Write your program in the provided places alone.

## Import bars.py 
import bars

def main():
    ### Write your code here
    n1=int(input("Enter the no.of times '*' should display:\n"))
    n2=int(input("Enter the no.of times '-' should display:\n"))
    n3=int(input("Enter the no.of times '#' should display:\n"))
    bars.draw_bar(n1,n2,n3)
    return



if __name__=='__main__':
    main()
    