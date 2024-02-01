dead=int(input("Dead Count: \n"))
if dead<0:
    print("Invalid input")
    quit()
injured=int(input("Injured Count: \n"))
if injured<0:
    print("Invalid input")
    quit()
safe=int(input("Safe Count: \n"))
if safe<0:
    print("Invalid input")
    quit()

print("\nTSUNAMI REPORT OF JAPAN")
print("The number of people")
print("Dead:"+str(dead))
print("Injured:"+str(injured))
print("Safe:"+str(safe))
print("Please help the people who are suffering!!!")