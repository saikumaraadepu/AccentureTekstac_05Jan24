import numpy as np

points=[]
print("Enter John's points for each quarter:")
for i in range(1,5):
    for j in range(1,5):
        point=int(input(f'Quarter {i}, Point {j}:\n'))
        points.append(point)
john_statistics=np.array(points).reshape(4,4)
print("John's Statistics:")
print(john_statistics)
total_points=np.sum(john_statistics[:2])
average_points=np.mean(john_statistics[-1])
print('\nTotal points scored by John in the first 2 quarters : {:.2f}'.format(total_points))
print('Average points scored by John in the last quarter: {:.2f}'.format(average_points))