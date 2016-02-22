def divide(n):
    divide_by = set()
    start = 1
    while start != 0 and not start in divide_by:
        if start < n:
            start *= 10 
        else:
            divide_by.add(start)
            start %= n
    return len(divide_by)


my_max = float('-inf')
d = -1

for n in range(2, 1000):
    temp = divide(n)
    if temp > my_max:
        my_max = temp
        d = n

print "d is equal to {} and the length of the cycle is {}".format(d, my_max)
