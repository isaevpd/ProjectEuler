def chain(n):
    num = n
    while True:
        temp = 0
        for s in str(num):
            temp += int(s) * int(s)
            # print num
        num = temp
        if num == 89:
            return True
        elif num == 1:
            return False

result = 0

for num in xrange(2, 10000000):
    print num
    if chain(num):
        result += 1


print 'Answer is ' + str(result)