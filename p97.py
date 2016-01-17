n = 2
for idx in xrange(1, 7830457):
    n *= 2
    n %= 10000000000

answer = str(28433 * n + 1)[-10:]
print answer