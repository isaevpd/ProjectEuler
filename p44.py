import math
def pent(n):
    return n * (3 * n - 1) / 2.

def ispent(n):
    return (1 + math.sqrt(24 * n + 1)) % 6 == 0

pj = 0
pk = 0
diff = float('inf')

numbers = set([pent(n) for n in xrange(1, 10000)])

for num1 in numbers:
    for num2 in numbers:
        tempdiff = abs(num1 - num2)
        if ispent(tempdiff):
            if ispent(num1 + num2) and tempdiff < diff:
                diff =  tempdiff
                pj = num1
                pk = num2

print diff, pj, pk