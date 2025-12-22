import random

num = int(input("How many times you want to flip?"))
coin = [0, 0]
if(num >= 0):
    for i in range(num):
        res = random.random()
        if res < 0.5:
            print("Tail")
            coin[0] += 1
        else:
            print("Heads")
            coin[1] += 1

print("Total number of heads: ", coin[1], " And total numebr of tails: ", coin[0])
print("Percentage of heads: ", coin[1] / num * 100 )
print("And number of tails: ", coin[0] / num * 100)

