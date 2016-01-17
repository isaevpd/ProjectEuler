from primeGen import primes2

def pand(n):
	return sorted(str(n)) == [str(n) for n in range(1, len(str(n)) + 1)]


primelst = primes2(100000000)
# primesset = set(primes)

largest = 0

print 'starting loop'

for num in primelst:
	if pand(num):
		largest = num


print largest
