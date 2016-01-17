from primeGen import get_primes

def trunc(n):
	temp = str(n)
	result = set()
	for idx in range(len(temp)):
		result.add(temp[idx:])
		result.add(temp[:idx])
	return {int(n) for n in result if n.isdigit()}

primes = get_primes(1000000)

final = set()
result = set()
for num1 in primes:
	for num2 in trunc(num1):
		flag = True
		if not num2 in primes:
			flag = False
			break
	if flag:
		result.add(num1)

for res in result:
	if res > 10:
		final.add(res)

print sum(final)

