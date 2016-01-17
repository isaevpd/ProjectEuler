from primeGen import get_primes

PRIMELST = (get_primes(100000))


def gen_inc(n):
	trial = [n, n + 3330, n + 3330 * 2]
	if len({''.join(sorted(str(num))) for num in trial}) == 1 and len(filter(lambda x: x in PRIMELST, trial)) == 3:
		return trial
	return False


for num in PRIMELST:
	if gen_inc(num):
		print gen_inc(num)
	if num > 9999:
		break