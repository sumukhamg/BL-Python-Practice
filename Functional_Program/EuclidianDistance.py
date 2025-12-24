import math

x = int(input("Enter x value: "))
y = int(input("Enter y value: "))

xsqr = x * x
ysqr = y * y

distance = math.sqrt(xsqr + ysqr)
print("The distanc is: ", distance)