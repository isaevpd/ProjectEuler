result = 1

for coin1 in xrange(201):
    print coin1
    for coin2 in xrange(0, 201, 2):
        if coin2 + coin1 > 200:
            break
        for coin3 in xrange(0, 201, 5):
            if coin2 + coin1 + coin3 > 200:
                break
            for coin4 in xrange(0, 201, 10):
                if coin1 + coin2 + coin3 + coin4 > 200:
                    break
                for coin5 in xrange(0, 201, 20):
                    for coin6 in xrange(0, 201, 50):
                        for coin7 in xrange(0, 201, 100):
                            if coin1 + coin2 + coin3 + coin4 + coin5 + coin6 + coin7 == 200:
                                result += 1



print result 