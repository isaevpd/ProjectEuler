import primeGen

def gen_rotations(n):
	result = set()
	temp = str(n)
	for idx in range(len(temp)):
		rotation = int(temp[idx:] + temp[:idx])
		result.add(rotation)
	return result


primes = primeGen.get_primes(1000000)

result = set()


for num1 in primes:
	#print num1
	for num2 in gen_rotations(num1):
		flag = True
		# print '2nd loop', num2, result
		if not (num2 in primes):
			flag = False
			break
	if flag:
		result.add(num1)



print len(result)