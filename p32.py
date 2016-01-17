product = set()

for num1 in xrange(2000):
	for num2 in xrange(2000):
		temp = num1 * num2
		if sorted(str(num1) + str(num2) + str(temp)) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
			product.add(temp)

print sum(product)