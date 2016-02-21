def divide(n):
    divide_by = list()
    start = 1
    while True:
        if start == 0:
            break
        if start < n:
            start *= 10 
        else:
            if start in divide_by:
                break
            divide_by.append(start)
            #print 'dividing {}/{} remainder is {}'.format(start, n, start % n)
            start = start % n

    return len(divide_by)


my_max = float('-inf')
result = -1

for n in range(2, 1000):
    temp = divide(n)
    if temp > my_max:
        my_max = temp
        result = n

print "d is equal to {} and the length of the cycle is {}".format(result, my_max)
