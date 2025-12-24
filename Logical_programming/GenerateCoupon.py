import random

n = int(input("Enter N"))
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'F']

# print(random.shuffle(str))


while( n > 0):
    random.shuffle(alpha)
    lett = random.sample(alpha, 3)
    num = random.randint(100, 999)
    coupon = ''.join(lett) + str(num)
    print(coupon)
    n -= 1
