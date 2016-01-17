import math
from primeGen import isPrime, primes2

PRIMELIST = primes2(1000000)


def isCompositeOdd(n):
    if n % 2 == 0:
        return False
    elif not isPrime(n):
        return True
    return False

def prop(n):
    topSquare = int(math.ceil(math.sqrt(n)))
    idx = 0
    for num in PRIMELIST:
        if num > n:
            idx = PRIMELIST.index(num)
            # print num
            break
    for index in range(idx + 1):
        for square in range(topSquare):
            if PRIMELIST[index] + 2 * square * square == n:
                # print PRIMELIST[index], square
                return True
    return False

nums = 33


while True:
    if isCompositeOdd(nums):
        if not prop(nums):
            print nums
            break
    nums += 1








