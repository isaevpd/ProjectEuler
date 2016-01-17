## runs 2 min in pypy brute force solution

def get_r(a, n):
    return ((a - 1) ** n + (a + 1) ** n) % (a * a)

def get_max_r(a):
    result = 0
    for n in xrange(2, 2000):
        temp = get_r(a, n)
        if temp > result:
            result = temp
    return result

result = 0

for a in xrange(3, 1001):
    result += get_max_r(a)

print result