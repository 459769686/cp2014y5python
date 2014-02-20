import math
def isPrime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0 : return False
    return True

k = 0
c = 0
n = 0
while(c<=999):    
    if isPrime(n):
        c = c + 1
        k = k + 1
        print("{0:>5.0f}".format(n), end="")
        if k == 10:
            print()
            k = 0
    n = n + 1
