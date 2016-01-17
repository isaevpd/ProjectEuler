import itertools, math


def p53():
	result = 0
	for n in range(23, 101):
		for r in range(1, n):
			temp = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
			if temp > 1e6:
				# print temp
				result += 1
	return result

print p53()
# print (tuple(itertools.combinations(range(1, 6), 2)))