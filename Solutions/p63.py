def test(n, power):
    return len(str(n ** power)) == power

result = set()
for num in xrange(1, 10000):
    for power in xrange(1, 50):
        if test(num, power):
            result.add(num ** power)


print (result)