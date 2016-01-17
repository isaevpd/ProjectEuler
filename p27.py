from primeGen import get_primes

def quad(n, a, b):
	return n * n + a * n + b

primes = get_primes(100000)
best = 0
counter = 0
coef_a = 0
coef_b = 0
#results = set()

for a in range(-999, 1000):
	for b in range(-999, 1000):
		n = 0
		while True:
			if not (quad(n, a, b) in primes):
				break
			else:
				counter += 1
				n += 1
			#results.add(quad(n, a, b))
		if counter >  best:
			best = counter
			coef_a = a
			coef_b = b
		counter = 0


# for i in range(15):
# 	print quad(i, 999, 999)

#print coef_a, coef_b




