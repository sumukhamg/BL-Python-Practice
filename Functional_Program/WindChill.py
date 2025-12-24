import math

t = int(input("Enter value of t"))
v = int(input("Enter value of v"))

if(t > 50 or v > 120):
    print("w cannot be calculated")
else:
    w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)
    print("Value of w: ",w)

