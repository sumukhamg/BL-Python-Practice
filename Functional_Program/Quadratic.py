import math

a = int(input("Enter  valus of a"))
b = int(input("Enter  valus of b"))
c = int(input("Enter  valus of c"))

delta = b*b - 4 * a * c
if(delta > 0):
    root1 = (-b + math.sqrt(delta)) / (2 * a)
    root2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Roots of equation: ", root1, " and ", root2)

else: 
    print("Roots are imaginary")