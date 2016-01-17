#doesnt work
from fractions import gcd
from primeGen import isPrime


def rPrime(a, b):
    return gcd(a, b) == 1


def phi(n):
    divs = 0
    for x in xrange(1, n):
        if rPrime(x, n):
            divs += 1
    return divs

print phi(9)

helper = 0
result = 0

for n in xrange(2, 10000):
    print n
    temp = float(n) / phi(n)
    # print phi(n), n
    if temp > helper:
        helper = temp
        result = n


print 'Answer is ' + str(result)


# print result

