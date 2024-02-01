
# Function to check Odd number
def checkOdd(N):
    if(N%2!=0):
        return True
    else:
        return False


# Function to check Automorphic number
def isAutomorphic(N) :
	sq = N * N
	while N!=0:
		if N % 10==sq % 10:
			return True
		else:
		    return False
		N//= 10
		sq//= 10
	

# Driver method
def main():
    print("Enter the number:")
    N=int(input('\n'))
    
    if checkOdd(N):
        if isAutomorphic(N):
            print("Automorphic Number")
        else :
	        print("Not an Automorphic Number")
    else:
	    print("Not an Odd Number")
	
	

if __name__=="__main__":
    main()
    
