from primeGen import primes2

PRIMELST = primes2(7071)

result = set()
for num1 in PRIMELST:
    for num2 in PRIMELST:
        for num3 in PRIMELST:
            temp = num1 * num1 + num2 ** 3 + num3 ** 4
            if temp < 5e7:
                result.add(temp)

print len(result)


