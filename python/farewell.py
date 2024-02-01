import greet

name=input("Enter the senior's name:\n")
print(greet.message,end=' ')
greet.greet(name)
print('Documentation string:',greet.greet.__doc__)