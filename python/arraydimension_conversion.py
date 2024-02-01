import numpy as np

pixels=[]
print('Enter pixel values for the image (8 values):')
for i in range(1,9):
    pixel=int(input(f'Pixel {i}:\n'))
    if pixel<0 or pixel>256:
        print('Invalid input! Enter a value between 0 and 256')
        continue
    pixels.append(pixel)
arr=np.array(pixels)
print(f'Original Array:\n{arr}')
image_matrix=arr.reshape(2,4)
print(f'\nImage Matrix (2x4):\n{image_matrix}')
print(f'\nTop-left 2x2 Region:\n{image_matrix[:1,:2]}')
print(f'\nBottom-right 2x2 Region:\n{image_matrix[1:,2:]}')
print('\nMean value of the pixel values in the Image matrix: {:.2f}'.format(np.mean(image_matrix)))