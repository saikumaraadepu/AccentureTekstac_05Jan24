def find_prime(n1,n2):
    if n1<0 or n2<0:
        return ['Invalid range']
    if n1>n2:
        return ['Invalid range']
    primes=[]
    for num in range(n1,n2+1):
        if num>1:
            for i in range(2,num):
                if (num%i)==0:
                    break
            else:
                primes.append(num)
    if not primes:
        return ['There are no prime numbers in this range']
    return primes

    
start,end=int(input('\n')),int(input('\n'))
res=find_prime(start,end)
result=''
for i in range(len(res)):
    result+=str(res[i])+' '
print(result.strip())