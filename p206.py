import math

num = 1000000000

def helper(x, n):
    return (x % (10 ** n)) / (10 ** (n - 1))

def check(n):
    assert(len(str(n)) == 19)
    count = 9
    # print count[9]
    for idx in xrange(3, 20, 2):
        # print "idx is " + str(idx)
        # print helper(n, idx)
        if helper(n, idx) != count:
            return False
        count -= 1
    return True

# print check(1020304050607080950)

while True:
    if helper(num, 1) == 0:
        print num
        if check(num ** 2):
            print (num)
            break
    num += 10
    # print num


