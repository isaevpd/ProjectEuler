#doesnt work

from primeGen import primes2

PRIMELST = primes2(1000000000)
PRIMESET = set(PRIMELST)
print 'done'

def pattern(n):
    if (n + 1) % 2 == 0:
        # print 'not'
        return False
    elif (n + 1) % 3 == 0:
        return False
    elif (n + 1) % 5 == 0:
        return False
    elif (n + 1) % 7 == 0:
        return False
    if n * n + 1 in PRIMESET:
        start = PRIMELST.index(n * n + 1)
    else:
        return False
    values = (3, 7, 9, 13, 27)
    primeValues = [PRIMELST[num] for num in xrange(start + 1, start + 6)]
    for idx in xrange(5):
        if not primeValues[idx] == n * n + values[idx]:
            return False
    return True

# print pattern(10)


result = 0
for num in xrange(1000000):
    # print num
    if pattern(num):
        result += num

print result
