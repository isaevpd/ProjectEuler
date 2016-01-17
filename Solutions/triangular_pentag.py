def triangle(n):
    return n * (n + 1) / 2.


def pentagonal(n):
    return n * (3 * n - 1) / 2.

def hexagonal(n):
    return n * (2 * n - 1)


##for n in range(1, 6):
##    print triangle(n),\
##          pentagonal(n),\
##          hexagonal(n)


##possible_numbers = set()
##
##for t in xrange(20000, 40000):
##    for p in xrange(15000, 30000):
##        #for h in range(143, 4000):
##        if triangle(t) == pentagonal(p):
##            # == hexagonal(h):
##            possible_numbers.add((triangle(t), t))
##
##print (possible_numbers)
