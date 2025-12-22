n = int(input("Enter the number"))

def isPrime(j):
    if j < 2:
        return False
    i = 2
    while i * i <= j:
        if j % i == 0:
            return False
        i += 1
    return True

for j in range(2, n):
    if isPrime(j) and n % j == 0:
        print(j)