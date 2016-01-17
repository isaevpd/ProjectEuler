from primeGen import primes2

PRIMELST = primes2(1000000)

def primeDivisors(number, divisors):
    result = 0
    for num in PRIMELST:
        if number % num == 0:
            result += 1
        if num > (number / 2.):
            break
        if result == divisors:
            return True
    return False



x = 1
y = 2
z = 3
b = 4
while True:
    if primeDivisors(x, 4) and primeDivisors(y, 4) and primeDivisors(z, 4) and primeDivisors(b, 4):
        print x, y, z, b
        break
    x += 1
    y += 1
    z += 1
    b += 1

