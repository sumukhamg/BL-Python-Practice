num = int(input("Enter number"))
sum = 0
if num == 0:
    print("Number shoul not be 0")
else:
    for i in range(1, num):
        sum += 1/i

print(sum)