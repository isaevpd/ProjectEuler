from primeGen import primes2

primelst = primes2(1000000)
primeset = set(primelst)

total = 0
longest = 0
best = 0
result = 0

for idx in range(len(primelst)):
	total = 0
	longest = 0
	for num in primelst[idx:]:
		total += 1
		longest += num
		if longest in primeset:
			if total > best:
				best = total
				result = longest

print result
print best

