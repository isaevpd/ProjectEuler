#too slow

def is_increasing(n):
    temp = str(n)
    for idx in xrange(len(temp) - 1):
        if temp[idx] > temp[idx + 1]:
            return False
    return True

def is_decreasing(n):
    temp = str(n)
    for idx in xrange(len(temp) - 1):
        if temp[idx] < temp[idx + 1]:
            return False
    return True


def main():
    result = 0
    for num in xrange(1, int(1e10)):
        if is_increasing(num) or is_decreasing(num):
            result += 1
            print num
            # print 'heres my bouncy', num
    return result

# print is_increasing(155349)
# print is_decreasing(155349)
print main()

