import numpy as np

days=int(input('Enter the number of days: \n'))
records=[]
print(f'Enter temperature records for {days} days:')
for i in range(1,days+1):
    temp=float(input(f'Day {i}: \n'))
    records.append(temp)
temperatures=np.array(records)
print(f'Temperature Records for the City:\n{temperatures}')
print(f'\nMean Temperature for {days} Days: {np.mean(temperatures):.2f}')
max_temp,max_day=np.max(temperatures),np.argmax(temperatures)+1
min_temp,min_day=np.min(temperatures),np.argmin(temperatures)+1
print(f'Day with the Highest Temperature: Day {max_day} Temperature: {max_temp}')
print(f'Day with the Lowest Temperature: Day {min_day} Temperature: {min_temp}')
sorted_index=np.argsort(records)
sorted_days=sorted_index+1
print(f'\nDays Sorted by Temperature (Ascending Order):')
for i in range(days):
    print(f'Day {sorted_days[i]}: Temperature {temperatures[sorted_index[i]]}')