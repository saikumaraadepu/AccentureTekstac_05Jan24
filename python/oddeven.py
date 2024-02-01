def operation(my_tuple):
    odd_sum=0
    even_sum=0
    for i in range(len(my_tuple)):
        if my_tuple[i]%2==0:
            even_sum=even_sum+my_tuple[i]
        else:
            odd_sum=odd_sum+my_tuple[i]
    return (even_sum,odd_sum)
    
    
my_tuple=(20,5,70,9,100)
sum_value=operation(my_tuple)

print("Sum of odd numbers :",sum_value[1])
print("Sum of even numbers :",sum_value[0])