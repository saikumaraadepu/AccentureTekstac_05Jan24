a4sheet=float(input("Cost of A4sheet:\n"))
if a4sheet<=0:
    print("Invalid input")
    quit()

pen=float(input("Cost of pen:\n"))
if pen<=0:
    print("Invalid input")
    quit()
    
pencil=float(input("Cost of pencil:\n"))
if pencil<=0:
    print("Invalid input")
    quit()
    
eraser=float(input("Cost of eraser:\n"))
if eraser<=0:
    print("Invalid input")
    quit()

print("Items Details")
print("A4sheet:%.2f" %a4sheet)
print("Pen:%.2f" %pen)
print("Pencil:%.2f" %pencil)
print("Eraser:%.2f" %eraser)