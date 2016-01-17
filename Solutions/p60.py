# #UNSOLVED!
from primeGen import primes2, FermatPrimalityTest

PRIMELST = set(primes2(10000))

print len(PRIMELST)

def prop(lst):
    for num1 in lst:
        for num2 in lst:
            a = int(str(num1) + str(num2))
            b = int(str(num2) + str(num1))
            if a != b:
                if not FermatPrimalityTest(a):
                    return False
                elif not FermatPrimalityTest(b):
                    return False
                else:
                    # print 'quitting', a, b
                    continue
    return True

# print 'test'
# print prop([3, 7, 109, 673])

result = float('inf')
for num1 in PRIMELST:
    for num2 in PRIMELST:
        if num1 != num2:
            if prop([num1, num2]):
                for num3 in PRIMELST:
                    if num3 != num2 and num3 != num1:
                        if prop([num1, num2, num3]):
                            for num4 in PRIMELST:
                                if num4 != num1 and num4 != num2 and num4 != num3:
                                    if prop([num1, num2, num3, num4]):
                                    #     temp = sum([num1, num2, num3, num4])
                                    #     if temp < result:
                                    #         result = temp
                                        # print 'result so far is ' + str(result)
                                        # print num1, num2, num3, num4
                                        for num5 in PRIMELST:
                                            if num5 != num1 and num5 != num2 and num5 != num3 and num5 != num4:
                                                if prop([num1, num2, num3, num4, num5]):
                                                    temp = sum([num1, num2, num3, num4, num5])
                                                    if temp < result:
                                                        result = temp
                                                        print 'result so far is ' + str(result)

            # temp = prop([3, 7, 109, 673, num])
            # if temp:
            #     result.append([num1, num2, num3, num4, num5])
    

print 'result = ' +str(result)

# print prop([3, 7, 109, 673, 55])

# for num1 in PRIMELST:
