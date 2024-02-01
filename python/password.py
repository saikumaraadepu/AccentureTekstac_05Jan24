total_plots=int(input('Enter the total no.of plots:\n'))
if total_plots<1 or total_plots>20:
    print('Invalid Input')
    quit()
plots=[]
print('Enter the numbers of each plot:')
for i in range(total_plots):
    plot=float(input())
    if plot<=0:
        print('Invalid Input')
        quit()
    plots.append(plot)
odd_sum=sum([i for i in plots if i%2!=0])
even_sum=sum([i for i in plots if i%2==0])
average=(odd_sum+even_sum)/2
print(f'The password for the file is: {average:.2f}')